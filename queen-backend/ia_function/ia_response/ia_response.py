
import os, requests,json,pathlib,sys
from flask import request, jsonify,Response
from pathlib import Path
#from tts import tts_gcp2


# Rutas donde se almacenarán temporalmente los datos

INPUT_FILE = pathlib.Path('queen-backend/ia_function/ia_response/input.txt').resolve()
CRITERIA_FILE = pathlib.Path('queen-backend/ia_function/ia_response/criteria.txt').resolve()


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
                complete_response = ""
                for chunk in response.iter_content(chunk_size=None):
                    if chunk:
                        try:
                            clear_chunk=chunk.decode('utf-8')
                            print(clear_chunk)
                            #clear_chunk=json.loads(clear_chunk)
                            #clean_text=clear_chunk.get("response","")
                            complete_response += clear_chunk
                            print(complete_response)  # Aquí podrías ir procesando los chunks si es necesario
                        except (json.JSONDecodeError, UnicodeDecodeError) as e:
                            print(f"error de decodificacion: {e}")
                # Si quieres devolver el resultado completo como un JSON al final:
                return {"result": {"response": complete_response}}
            else:
                return {"error": f"Error: {response.status_code} - {response.text}"}
        else:
            # Si el stream no está activado, devolvemos el JSON completo
            response.raise_for_status()
            return response.json()
    except requests.exceptions.Timeout:
        return {"error": f"La solicitud ha superado el tiempo máximo de {timeout} segundos"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

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

    # Guardar el ensayo en un archivo temporal o procesarlo
    with open(INPUT_FILE, 'w') as f:
        f.write(input_text)

    return {"message": "Ensayo enviado con éxito."}

# Función para ejecutar la IA una vez que ambos, ensayo y criterios, estén listos
import os
import json

def process_response():
    # Verificar que tanto el ensayo como los criterios existan
    if not os.path.exists(INPUT_FILE) or not os.path.exists(CRITERIA_FILE):
        yield json.dumps({"message": "Aún faltan datos. Asegúrate de que el estudiante haya enviado el ensayo y el profesor los criterios."})
        return

    # Leer el ensayo y los criterios
    with open(INPUT_FILE, 'r') as f:
        input_text = f.read()
        #yield f"Texto del ensayo leído: {input_text}\n"

    with open(CRITERIA_FILE, 'r') as f:
        criteria = f.read()
        #yield f"Criterios leídos: {criteria}\n"

    # Asignar el rol y construir los inputs para la IA
    role_text = "Usted es un asistente de redacción académica..."
    system_instructions = f"{role_text} {criteria}"

    inputs = [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": input_text}
    ]

    # Simulación de llamada al modelo de IA (debe cambiarse por la real)
    result = run_model("@cf/meta/llama-3-8b-instruct", inputs, timeout=1200, stream=True)

    if 'error' in result:
        yield json.dumps({"message": "Error al procesar la solicitud: " + result['error']})
        return

    try:
        if 'result' in result and 'response' in result['result']:
            ai_response = result['result']['response']
            yield f"Respuesta de la IA: {ai_response}\n"
        else:
            yield json.dumps({"message": "Error al procesar la respuesta de la IA: no se encontró 'response'."})
    except KeyError:
        yield json.dumps({"message": "Error al procesar la respuesta de la IA."})

    
#process_response()