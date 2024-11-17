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
data = {
    "student_questions": [
        "¿podrias repetir Qué puedo mejorar en la argumentacion?"
    ]
}


if "VERCEL_ENV" in os.environ:  # Esta variable solo existe en Vercel
    INPUT_file_path = 'tmp/input.json'
    CRITERIA_file_path = 'ia_response/criteria.json'
    INTERACTIONS_file_path = 'ia_response/user_interactions/interactions.json'
    TTS_file_path = 'ia_response/cleanOutput.mp3'
else:
    INPUT_file_path = pathlib.Path('input.json').resolve()
    # print(INPUT_file_path)
    CRITERIA_file_path =  pathlib.Path('criteria.json').resolve()
    # print(CRITERIA_file_path)
    INTERACTIONS_file_path = pathlib.Path('ia_response/user_interactions/interactions.json').resolve()

    #print(INTERACTIONS_file_path)
    TTS_file_path = 'server_ia/ia_response/cleanOutput.mp3'


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
    # print(system_instructions)
    # print(inputs)
    with client.messages.stream(
        max_tokens=512,
        system=system_instructions,
        messages=inputs,
        model=model,
    )as stream:
        for text in stream.text_stream:
           yield text


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
            question = interaction.get('question', '').strip()
            response = interaction.get('response', '').strip()
            if question:
                inputs.append({"role": "user", "content": question})
            if response:
                inputs.append({"role": "assistant", "content": response})
    # Agregar los criterios de evaluación
    system_instructions = f"{role_text} Los criterios de evaluación son: {criteria}  Además, responda cualquier pregunta que el estudiante pueda tener sobre su evaluación."
    inputs.append({"role": "user", "content": input_text})

    # Agregar preguntas del estudiante si las hay
    if student_questions:
        print(f"Añadiendo pregunta del estudiante: {student_questions}")  # Depuración
        inputs.append({"role": "user", "content": student_questions})
    
    return system_instructions,inputs

# Función para obtener las últimas dos interacciones guardadas
def get_last_two_interactions():
    if os.path.exists(INTERACTIONS_file_path):
        with open(INTERACTIONS_file_path, 'r') as f:
            data = json.load(f)
            interactions = data.get("interactions", [])
        # Extraer las dos últimas interacciones
        return interactions[-2:] if len(interactions) >= 2 else interactions
    return []

# Función para enviar los criterios y evaluar si el ensayo ya fue enviado
def submit_criteria(data):
    criteria = data.get('criteria')
    
    # Guardar los criterios en un archivo JSON si aún no están guardados
    if not os.path.exists(CRITERIA_file_path):
        save_json(CRITERIA_file_path, data)
        print("Criterios guardados.")
    else:
        print("Los criterios ya han sido enviados anteriormente.")
    
    # Intentar evaluar si el ensayo está disponible
    if os.path.exists(INPUT_file_path):
        return evaluate_essay()
    else:
        return {"message": "Criterios enviados con éxito. Esperando el ensayo del estudiante."}

# Función para enviar el ensayo
def submit_essay(data):
    
    # Guardar el ensayo en un archivo JSON si aún no está guardado
    if not os.path.exists(INPUT_file_path):
        save_json(INPUT_file_path, data)
        print("Ensayo guardado.")
    else:
        print("El ensayo ya ha sido enviado anteriormente. sobreescribiendo datos...")
        save_json(INPUT_file_path,data)

    # Intentar evaluar si los criterios están disponibles
    if os.path.exists(CRITERIA_file_path):
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
    if os.path.exists(INTERACTIONS_file_path):
        with open(INTERACTIONS_file_path, 'r') as f:
            interactions_data = json.load(f)
    else:
        # Si el archivo no existe, crear una estructura nueva con un ID único para el archivo
        interactions_data = {
            "conversation_id": str(ObjectId()),  # ID único para el archivo
            "interactions": []  # Lista vacía para almacenar las interacciones
        }

    # Agregar la nueva interacción y guardar en el archivo
    interactions_data["interactions"].append(interaction)
    with open(INTERACTIONS_file_path, 'w') as f:
        json.dump(interactions_data, f, indent=4)


# Función para procesar preguntas del estudiante y respuestas de la IA
def process_questions_and_responses(student_questions):
    # Verificar que existan el ensayo y los criterios
    if not os.path.exists(INPUT_file_path) or not os.path.exists(CRITERIA_file_path):
        return {
            "message": "Aún faltan datos. Asegúrate de que el estudiante haya enviado el ensayo y el profesor los criterios."}


    # Leer ensayo y criterios
    input_text = load_data_from_file(INPUT_file_path, 'input')
    #print(f"Ensayo cargado: {input_text}")

    criteria = load_data_from_file(CRITERIA_file_path, 'criteria')
    #print(f"Criterios cargados: {criteria}")

    # Asegurarse de que existan preguntas del estudiante
    if not student_questions:
        return {"message": "No se proporcionaron preguntas del estudiante."}

    # Procesar cada pregunta con el modelo IA (suponiendo que tienes una función `evaluate_question`)
    responses = []
    for question in student_questions:
        system_instructions, inputs = generate_inputs(input_text, criteria, question)
        result_stream = run_model("claude-3-5-sonnet-20241022", system_instructions, inputs)
        return process_ia_response(result_stream, input_text, student_questions)

        # response_text = "".join(result_stream)
        # responses.append({"question": question, "response": response_text})
        # print(f"Pregunta: {question}, Respuesta: {response_text}")

    # Retornar todas las respuestas como JSON


# Funciones auxiliares
def save_json(file_path, data):
    """Guarda los datos en un archivo JSON con formato legible."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Función para evaluar el ensayo si ambos archivos están disponibles
def evaluate_essay():
    # Cargar ensayo y criterios
    input_text = load_data_from_file(INPUT_file_path, 'input')
    criteria = load_data_from_file(CRITERIA_file_path, 'criteria')
    # Verificar que existan ambos archivos
    if not input_text or not criteria:
        return {"message": "Aún faltan datos para evaluar el ensayo."}
    # Generar entradas y procesar evaluación en la IA
    system_instructions,inputs = generate_inputs(input_text, criteria)
    result_stream=run_model("claude-3-5-sonnet-20241022", system_instructions,inputs)
    for text in process_ia_response(result_stream, input_text):
           yield text

def process_ia_response(result_stream, input_text, student_questions=None):
    """Procesa la respuesta del modelo IA y guarda la interacción en el archivo JSON."""
    response_text = ""
    try:
         # Enviar las últimas dos interacciones al cliente, si están disponibles
        print("intentando procesar el stream de respuesta de la IA")
        for text in result_stream:
            response_text += text
            yield f"data: {json.dumps({'text': text})}\n\n"

        # Guardar la interacción en el archivo JSON
        clean_text=tts_gcp2.procesar_texto(response_text)
        print(clean_text)
        # tts_gcp2.run_and_save(clean_text,TTS_FILE) TODO: Descomentar esta línea para habilitar la generación de audio
        if student_questions:
            for question in student_questions:
                save_interaction(question, response_text, interaction_type="question")
        else:
            save_interaction(input_text, response_text, interaction_type="essay")
    except Exception as e:
        yield json.dumps({"message": f"Error al procesar la respuesta de la IA: {str(e)}"})

# for text in process_questions_and_responses(data.get("student_questions")):
#     print(text,end="",flush=True)
