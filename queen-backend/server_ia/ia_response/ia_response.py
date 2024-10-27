import os, requests,json,pathlib
#from tts import tts_gcp2


# Rutas donde se almacenarán temporalmente los datos

INPUT_FILE = pathlib.Path('queen-backend/server_ia/ia_response/input.json').resolve()
CRITERIA_FILE = pathlib.Path('queen-backend/server_ia/ia_response/criteria.json').resolve()
INTERACTIONS_FILE =pathlib.Path('queen-backend/server_ia/ia_response/interactions.json').resolve()


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

def submit_criteria(data):
    criteria = data.get('criteria')  # Obtén los criterios del diccionario `data`

    # Guardar los criterios en un archivo JSON
    with open(CRITERIA_FILE, 'w') as f:
        json.dump({"criteria": criteria}, f, indent=4)  # Guarda los criterios en formato JSON con indentación

    return {"message": "Criterios enviados con éxito. Procesando la revisión."}


def submit(data):
    # Procesar el data como sea necesario
    input_text = data.get('input')  # Asegúrate de que 'input' esté en los datos
    print(INPUT_FILE)

    # Guardar el ensayo en un archivo JSON
    with open(INPUT_FILE, 'w') as f:
        json.dump(data, f, indent=4)  # Escribe data en formato JSON con indentación de 4 espacios

    return {"message": "Ensayo enviado con éxito. Esperando criterios del profesor."}
# Función para ejecutar la IA una vez que ambos, ensayo y criterios, estén listos
def save_interaction(question, response):
    interaction = {
        "question": question,
        "response": response
    }
     # Verificar si el archivo de interacciones ya existe y cargarlo
    if os.path.exists(INTERACTIONS_FILE):
        with open(INTERACTIONS_FILE, 'r') as f:
            interactions = json.load(f)
    else:
        interactions = []

    # Agregar la nueva interacción y guardar en el archivo
    interactions.append(interaction)
    with open(INTERACTIONS_FILE, 'w') as f:
        json.dump(interactions, f, indent=4)

def process_response(student_questions):
    # Verificar que tanto el ensayo como los criterios existan
    if not os.path.exists(INPUT_FILE) or not os.path.exists(CRITERIA_FILE):
        return ({"message": "Aún faltan datos. Asegúrate de que el estudiante haya enviado el ensayo y el profesor los criterios."})

    # Leer el ensayo y los criterios desde los archivos JSON
    with open(INPUT_FILE, 'r') as f:
        input_data = json.load(f)  # Cargar el contenido del archivo como JSON
        input_text = input_data.get('input')  # Extraer el texto del ensayo

    with open(CRITERIA_FILE, 'r') as f:
        criteria_data = json.load(f)  # Cargar el contenido del archivo como JSON
        criteria = criteria_data.get('criteria')  # Extraer los criterios

    role_text = (
        "Usted es un asistente de redacción académica. Por favor, evalúe el ensayo "
        "centrándose en los siguientes aspectos y puntúe los ensayos de 0 a 10. "
        "Además, responda cualquier pregunta que el estudiante pueda tener sobre su evaluación."
    )
    system_instructions = f"{role_text} Los criterios de evaluación son: {criteria}"

    # Crear el input principal para la IA
    inputs = [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": input_text}
    ]

    # Si el estudiante tiene preguntas adicionales, añádelas al input
    if student_questions:
        for question in student_questions:
            inputs.append({"role": "user", "content": question})

    # Llamada al modelo de IA con stream
    result = run_model("@cf/meta/llama-3-8b-instruct", inputs, timeout=1200, stream=True)

    try:
        response_text = ""
        for fragment in result:
            response_text += fragment
            yield fragment  # Enviar cada fragmento en tiempo real

        # Guardar la interacción de pregunta-respuesta en el archivo JSON
        for question in student_questions:
            save_interaction(question, response_text)
    except Exception as e:
        yield json.dumps({"message": f"Error al procesar la respuesta de la IA: {str(e)}"})
