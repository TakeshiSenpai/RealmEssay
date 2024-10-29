import os, requests,json,pathlib,sys
from traceback import print_tb

sys.path.append(str(pathlib.Path(__file__).parent.resolve()))
#print(str(pathlib.Path(__file__).parent.resolve()))
from tts import tts_gcp2
from bson.objectid import ObjectId

# Rutas donde se almacenarán temporalmente los datos


#Revisen el pahtfile!!!
#A mi(Manuel) me fallo por eso
INPUT_FILE = pathlib.Path('server_ia/ia_response/input.json').resolve()
CRITERIA_FILE = pathlib.Path('server_ia/ia_response/criteria.json').resolve()
INTERACTIONS_FILE =pathlib.Path('queen-backend/server_ia/ia_response/user_interactions/interactions.json').resolve()
TTS_FILE=pathlib.Path('queen-backend/server_ia/ia_response/cleanOutput.mp3').resolve()


# Cargar el token desde un archivo
def load_api_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()  # Elimina espacios en blanco no deseados

# la URL base de la API, SOLO USAR GATEWAYLOG!!!
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/a71faaf431a55b28fbf7c2bfbe9c1fba/ai/run/"
API_BASE_GATEWAYLOG = "https://gateway.ai.cloudflare.com/v1/a71faaf431a55b28fbf7c2bfbe9c1fba/realm-es/workers-ai/"
# Cargar el token de la API desde el archivo
directorio_raiz = pathlib.Path(__file__).parent
api_token = load_api_token(pathlib.Path(directorio_raiz / 'model_authentication'/ 'api_token.txt'))

def run_model(model, inputs, timeout=1200, stream=True):
    headers = {"Authorization": f"Bearer {api_token}"}
    input_data = {"messages": inputs, "stream": stream}

    try:
        # Enviar la solicitud
        response = requests.post(f"{API_BASE_GATEWAYLOG}{model}", headers=headers, json=input_data, timeout=timeout, stream=stream)
        
        # Procesar respuesta en modo streaming
        if stream:
            if response.status_code == 200:
                # Itera sobre el contenido en fragmentos
                for chunk in response.iter_content(chunk_size=None):
                    if chunk:
                        try:
                            # Decodificar y limpiar el fragmento
                            clear_chunk = chunk.decode('utf-8')
                            start = clear_chunk.find('"response":"')
                            if start != -1:
                                start += len('"response":"')
                                end = clear_chunk.find('"', start)
                                if end != -1:
                                    clean_text = clear_chunk[start:end]
                                    yield clean_text  # Enviar cada fragmento de texto al instante
                        except UnicodeDecodeError as e:
                            print(f"Error de decodificación: {e}")
            else:
                yield json.dumps({"error": f"Error: {response.status_code} - {response.text}"})
        else:
            # Procesar respuesta completa cuando no es en streaming
            response.raise_for_status()
            yield response.json()  # Devolver el JSON completo si stream=False

    except requests.exceptions.Timeout:
        yield json.dumps({"error": f"La solicitud ha superado el tiempo máximo de {timeout} segundos"})
    except requests.exceptions.RequestException as e:
        yield json.dumps({"error": str(e)})

# Función para obtener las últimas dos interacciones guardadas
def get_last_two_interactions():
    if os.path.exists(INTERACTIONS_FILE):
        with open(INTERACTIONS_FILE, 'r') as f:
            data = json.load(f)
            interactions = data.get("interactions", [])
        # Extraer las dos últimas interacciones
        return interactions[-2:] if len(interactions) >= 2 else interactions
    return []

# Función para enviar los criterios y evaluar si el ensayo ya fue enviado
def submit_criteria(data):
    criteria = data.get('criteria')
    
    # Guardar los criterios en un archivo JSON si aún no están guardados
    if not os.path.exists(CRITERIA_FILE):
        save_json(CRITERIA_FILE, data)
        print("Criterios guardados.")
    else:
        print("Los criterios ya han sido enviados anteriormente.")
    
    # Intentar evaluar si el ensayo está disponible
    if os.path.exists(INPUT_FILE):
        return evaluate_essay()
    else:
        return {"message": "Criterios enviados con éxito. Esperando el ensayo del estudiante."}

# Función para enviar el ensayo
def submit_essay(data):
    input_text = data.get('input')
    
    # Guardar el ensayo en un archivo JSON si aún no está guardado
    if not os.path.exists(INPUT_FILE):
        save_json(INPUT_FILE, data)
        print("Ensayo guardado.")
    else:
        print("El ensayo ya ha sido enviado anteriormente. sobreescribiendo datos...")
        save_json(INPUT_FILE,data)

    # Intentar evaluar si los criterios están disponibles
    if os.path.exists(CRITERIA_FILE):
        return evaluate_essay()
    else:
        return {"message": "Ensayo enviado con éxito. Esperando criterios del profesor."}


def save_interaction(input_text, response, interaction_type="essay"):
    # Crear la interacción según el tipo
    if interaction_type == "question":
        interaction = {
            "question": input_text,
            "response": response
        }
    elif interaction_type == "essay":
        interaction = {
            "essay": input_text,
            "evaluation": response
        }
    else:
        raise ValueError("Tipo de interacción desconocido. Use 'question' o 'essay'.")

    # Verificar si el archivo de interacciones ya existe y cargarlo
    if os.path.exists(INTERACTIONS_FILE):
        with open(INTERACTIONS_FILE, 'r') as f:
            interactions_data = json.load(f)
    else:
        # Si el archivo no existe, crear una estructura nueva con un ID único para el archivo
        interactions_data = {
            "conversation_id": str(ObjectId()),  # ID único para el archivo
            "interactions": []  # Lista vacía para almacenar las interacciones
        }

    # Agregar la nueva interacción y guardar en el archivo
    interactions_data["interactions"].append(interaction)
    with open(INTERACTIONS_FILE, 'w') as f:
        json.dump(interactions_data, f, indent=4)
# Función para procesar preguntas del estudiante y respuestas de la IA
def process_questions_and_responses(student_questions):
    # Verificar que existan el ensayo y los criterios
    if not os.path.exists(INPUT_FILE) or not os.path.exists(CRITERIA_FILE):
        return {"message": "Aún faltan datos. Asegúrate de que el estudiante haya enviado el ensayo y el profesor los criterios."}
    print("Entro a  process_questions_and_responses")
    # Leer ensayo y criterios
    input_text = load_data_from_file(INPUT_FILE, 'input')
    criteria = load_data_from_file(CRITERIA_FILE, 'criteria')

    # Generar entradas para la IA con preguntas adicionales
    inputs = generate_inputs(input_text, criteria, student_questions)
    result_stream = run_model("@cf/meta/llama-3-8b-instruct", inputs, timeout=1200, stream=True)
    
    yield from process_ia_response(result_stream, input_text, student_questions)

# Funciones auxiliares
def save_json(file_path, data):
    """Guarda los datos en un archivo JSON con formato legible."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_data_from_file(file_path, key):
    """Carga un valor específico de un archivo JSON."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get(key)
    return None

def generate_inputs(input_text, criteria, student_questions=None):
    """Genera las entradas necesarias para el modelo de IA, incluyendo las últimas interacciones."""
    # Obtener las últimas dos interacciones para proporcionar contexto
    last_interactions = get_last_two_interactions()
    
    # Preparar el texto de instrucciones del sistema
    role_text = (
        "Usted es un asistente de redacción académica. Por favor, evalúe el ensayo "
        "centrándose en los siguientes aspectos y puntúe los ensayos de 0 a 10. "
    )
    if student_questions:
        role_text += "Además, responda cualquier pregunta que el estudiante pueda tener sobre su evaluación."
    
    # Incluir las interacciones anteriores, si las hay
    if last_interactions:
        role_text += " A continuación, se incluyen las últimas interacciones para proporcionar contexto:\n"
        for interaction in last_interactions:
            role_text += f"- Pregunta: {interaction.get('question', '')}\n"
            role_text += f"- Respuesta: {interaction.get('response', '')}\n"
    
    # Agregar los criterios de evaluación
    system_instructions = f"{role_text} Los criterios de evaluación son: {criteria}"
    inputs = [{"role": "system", "content": system_instructions}, {"role": "user", "content": input_text}]

    # Agregar preguntas del estudiante si las hay
    if student_questions:
        inputs.extend({"role": "user", "content": question} for question in student_questions)
    
    return inputs

# Función para evaluar el ensayo si ambos archivos están disponibles
def evaluate_essay():
    # Cargar ensayo y criterios
    input_text = load_data_from_file(INPUT_FILE, 'input')
    criteria = load_data_from_file(CRITERIA_FILE, 'criteria')

    # Verificar que existan ambos archivos
    if not input_text or not criteria:
        return {"message": "Aún faltan datos para evaluar el ensayo."}

    # Generar entradas y procesar evaluación en la IA
    inputs = generate_inputs(input_text, criteria)
    result_stream = run_model("@cf/meta/llama-3-8b-instruct", inputs, timeout=1200, stream=True)
    
    return process_ia_response(result_stream, input_text)

def process_ia_response(result_stream, input_text, student_questions=None):
    """Procesa la respuesta del modelo IA y guarda la interacción en el archivo JSON."""
    response_text = ""
    try:
         # Enviar las últimas dos interacciones al cliente, si están disponibles
     
        for fragment in result_stream:
            response_text += fragment
            yield fragment  # Enviar cada fragmento en tiempo real
        
        # Guardar la interacción en el archivo JSON
        clean_text=tts_gcp2.procesar_texto(response_text)
        print(clean_text)
        tts_gcp2.run_and_save(clean_text,TTS_FILE)
        if student_questions:
            for question in student_questions:
                save_interaction(question, response_text, interaction_type="question")
        else:
            save_interaction(input_text, response_text, interaction_type="essay")
    except Exception as e:
        yield json.dumps({"message": f"Error al procesar la respuesta de la IA: {str(e)}"})
