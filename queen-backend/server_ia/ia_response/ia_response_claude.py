import json
import os
import pathlib
import sys
import anthropic
sys.path.append(str(pathlib.Path(__file__).parent.resolve()))
#print(str(pathlib.Path(__file__).parent.resolve()))
from tts import tts_gcp2
from bson.objectid import ObjectId

# Rutas donde se almacenarán temporalmente los datos
def load_data_from_file(file_path, key):
    """Carga un valor específico de un archivo JSON."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get(key)
    return None


#Revisen el pahtfile!!!
#A mi(Manuel) me fallo por eso
INPUT_FILE = pathlib.Path('input.json').resolve()
#print(INPUT_FILE) #only for debugging
CRITERIA_FILE = pathlib.Path('criteria.json').resolve()
#print(CRITERIA_FILE) #only for debugging
INTERACTIONS_FILE =pathlib.Path('user_interactions/interactions.json').resolve()
print(INTERACTIONS_FILE)
TTS_FILE=pathlib.Path('server_ia/ia_response/cleanOutput.mp3').resolve()


# Cargar el token desde un archivo
def load_api_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()  # Elimina espacios en blanco no deseados


# Cargar el token de la API desde el archivo
directorio_raiz = pathlib.Path(__file__).parent
client = anthropic.Anthropic(
    api_key = load_api_token(pathlib.Path(directorio_raiz / 'model_authentication'/ 'claude_api_token.txt'))
)

def run_model(model,system_instructions,inputs):
    print(system_instructions)
    print(inputs[0])
    with client.messages.stream(
        max_tokens=512,
        system=system_instructions,
        messages=inputs,
        model=model,
    )as stream:
        for text in stream.text_stream:
           yield(text)


def generate_inputs(input_text ,criteria, student_questions=None):
    """Genera las entradas necesarias para el modelo de IA, incluyendo las últimas interacciones."""
    # Obtener las últimas dos interacciones para proporcionar contexto
    last_interactions = get_last_two_interactions()
    inputs=[]
    # Preparar el texto de instrucciones del sistema
    role_text = (
        "Usted es un asistente evaluador de ensayos de preparatoria y universidad. "
    )

    # Incluir las interacciones anteriores, si las hay
    if last_interactions:
        for interaction in last_interactions:
            inputs.append({"role": "user", "content": interaction.get('question', '')})
            inputs.append({"role": "assistant", "content": interaction.get('response', '')})

    # Agregar los criterios de evaluación
    system_instructions = f"{role_text} Los criterios de evaluación son: {criteria}  Además, responda cualquier pregunta que el estudiante pueda tener sobre su evaluación."
    inputs.append({"role": "user", "content": input_text})

    # Agregar preguntas del estudiante si las hay
    if student_questions:
        inputs.extend({"role": "user", "content": question} for question in student_questions)
    
    return system_instructions,inputs

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
    system_instructions,inputs = generate_inputs(input_text, criteria, student_questions)
    result_stream = run_model("claude-3-5-sonnet-20241022",system_instructions ,inputs)
    
    yield from process_ia_response(result_stream, input_text, student_questions)

# Funciones auxiliares
def save_json(file_path, data):
    """Guarda los datos en un archivo JSON con formato legible."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Función para evaluar el ensayo si ambos archivos están disponibles
def evaluate_essay():
    # Cargar ensayo y criterios
    input_text = load_data_from_file(INPUT_FILE, 'input')
    criteria = load_data_from_file(CRITERIA_FILE, 'criteria')

    # Verificar que existan ambos archivos
    if not input_text or not criteria:
        return {"message": "Aún faltan datos para evaluar el ensayo."}

    # Generar entradas y procesar evaluación en la IA
    system_instructions,inputs = generate_inputs(input_text, criteria)
    result_stream=run_model("claude-3-5-sonnet-20241022", system_instructions,inputs)
    
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
        # tts_gcp2.run_and_save(clean_text,TTS_FILE) TODO: Descomentar esta línea para habilitar la generación de audio
        if student_questions:
            for question in student_questions:
                save_interaction(question, response_text, interaction_type="question")
        else:
            save_interaction(input_text, response_text, interaction_type="essay")
    except Exception as e:
        yield json.dumps({"message": f"Error al procesar la respuesta de la IA: {str(e)}"})

evaluate_essay()



