
import os, requests,json,pathlib
from flask import request, jsonify,Response
from pathlib import Path
#from tts import tts_gcp2


# Rutas donde se almacenarán temporalmente los datos

INPUT_FILE = pathlib.Path('input.txt').resolve()
CRITERIA_FILE = pathlib.Path('criteria.txt').resolve()


# Cargar el token desde un archivo
def load_api_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()  # Elimina espacios en blanco no deseados

# Definir la URL base de la API
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/a71faaf431a55b28fbf7c2bfbe9c1fba/ai/run/"

# Cargar el token de la API desde el archivo
directorio_raiz = Path(__file__).parent
api_token = load_api_token(pathlib.Path(directorio_raiz / 'model_authentication'/ 'api_token.txt'))


def run_model(model, inputs, timeout=1200, stream=True):
    headers = {"Authorization": f"Bearer {api_token}"}
    input_data = {"messages": inputs, "stream": stream}

    try:
        # Enviar la solicitud
        response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input_data, timeout=timeout, stream=stream)

        if stream:
            # Si el stream está activado, procesamos la respuesta en fragmentos
            if response.status_code == 200:
                
                # Streaming de datos al frontend
                for chunk in response.iter_content(chunk_size=None):
                    if chunk:
                        try:
                            # Decodificar el fragmento en string
                            clear_chunk = chunk.decode('utf-8')

                            # Verificar si contiene el campo "response"
                            start = clear_chunk.find('"response":"')
                            if start != -1:
                                start += len('"response":"')  # Ajustamos la posición para después de "response":" 
                                end = clear_chunk.find('"', start)

                                if end != -1:
                                    # Extraer y acumular el texto limpio
                                    clean_text = clear_chunk[start:end]
                                    print(f"Extracto: {clean_text}")
                                    yield f"data:{clean_text}\n\n"
                        except (UnicodeDecodeError) as e:
                            print(f"Error de decodificación: {e}")
            else:
                # Manejo de errores en la respuesta HTTP
                yield f"data: Error: {response.status_code} - {response.text}\n\n"
        else:
            # Si el stream no está activado, devolvemos el JSON completo de una vez
            response.raise_for_status()
            yield response

    except requests.exceptions.Timeout:
        yield f"data: Error: La solicitud ha superado el tiempo máximo de {timeout} segundos\n\n"
    except requests.exceptions.RequestException as e:
        yield f"data: Error: {str(e)}\n\n"

# Ruta para que el profesor envíe los criterios de evaluación
def submit_criteria(data):
    data=request.json
    criteria = data.get('criteria')  # Criterios proporcionados por el profesor

    # Guardar los criterios en un archivo temporal
    with open(CRITERIA_FILE, 'w') as f:
        f.write(criteria)

    return jsonify({"message": "Criterios enviados con éxito. Procesando la revisión."})
# Ruta para que el estudiante envíe el ensayo o sus preguntas hacia la IA
# En ia_response.py

def submit(data):
    # Procesar el data como sea necesario
    input_text = data.get('input')  # Asegúrate de que 'input' esté en los datos
    print(INPUT_FILE)
    # Guardar el ensayo en un archivo temporal o procesarlo
    with open(INPUT_FILE, 'w') as f:
        f.write(input_text)

    return {"message": "Ensayo enviado con éxito."}

# Función para ejecutar la IA una vez que ambos, ensayo y criterios, estén listos
def process_response():
    # Verificar que tanto el ensayo como los criterios existan
    if not os.path.exists(INPUT_FILE) or not os.path.exists(CRITERIA_FILE):
        return jsonify({"message": "Aún faltan datos. Asegúrate de que el estudiante haya enviado el ensayo y el profesor los criterios."})

    # Leer el ensayo y los criterios
    with open(INPUT_FILE, 'r') as f:
        input_text = f.read()

    with open(CRITERIA_FILE, 'r') as f:
        criteria = f.read()

    # Asignar el rol y construir los inputs para la IA
    role_text = "Usted es un asistente de redacción académica. Por favor, evalúe el ensayo centrándose en los siguientes aspectos y puntúe los ensayos de 0 a 10 y responda las posibles preguntas de los alumnos hagan sobre su evaluacion."
    system_instructions = f"{role_text} {criteria}"

    # Inputs para la IA
    inputs = [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": input_text}
    ]

    # Crear una función generadora que procese y envíe fragmentos de datos
    def generate_response():
        result_gen = run_model("@cf/meta/llama-3-8b-instruct", inputs, timeout=1200, stream=True)
        
        complete_response = ""  # Variable para almacenar el texto completo

        # Iterar sobre el generador y enviar los fragmentos al frontend
        for chunk in result_gen:
            if chunk:  # Asegúrate de no enviar fragmentos vacíos
                complete_response += chunk  # Acumular el texto completo
                yield f"data: {chunk}\n\n"  # Enviar los fragmentos al frontend

        # Al final del stream, enviar el mensaje de finalización
        yield "data: [DONE]\n\n"

        # Aquí puedes realizar el TTS con el texto completo
        # Por ejemplo, pasarlo a una función TTS para generar el archivo de audio
        print("Texto completo para TTS:", complete_response)
        # Supongamos que tienes una función `generate_tts` para procesar el texto completo
        #tts_gcp2.run_and_save(complete_response, "output.mp3")

    # Crear la respuesta como un stream y enviarla al frontend

