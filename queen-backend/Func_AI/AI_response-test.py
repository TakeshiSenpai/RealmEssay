import os,requests,TTS_GCP2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Rutas donde se almacenarán temporalmente los datos

ESSAY_FILE = "queen-backend\\Func_AI\\essay.txt"
CRITERIA_FILE = "queen-backend\\Func_AI\\criteria.txt"


# Cargar el token desde un archivo
def load_api_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()  # Elimina espacios en blanco no deseados

# Definir la URL base de la API
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/a71faaf431a55b28fbf7c2bfbe9c1fba/ai/run/"

# Cargar el token de la API desde el archivo
api_token = load_api_token('queen-backend\\Func_AI\\Auth\\API_token.txt')


# Función para ejecutar el modelo
def run_model(model, inputs, timeout=1200):
    headers = {"Authorization": f"Bearer {api_token}"}
    input_data = { "messages": inputs }
    try:
        response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input_data, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": f"La solicitud ha superado el tiempo máximo de {timeout} segundos"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Ruta para que el estudiante envíe el ensayo
@app.route('/submit_essay', methods=['POST'])
def submit_essay():
    data=request.json
    essay_text = data.get('essay')  # Obtenemos el texto enviado por el estudiante

    # Guardar el ensayo en un archivo temporal
    with open(ESSAY_FILE, 'w') as f:
        f.write(essay_text)

    return jsonify({"message": "Ensayo enviado con éxito. Esperando criterios del profesor."})

# Ruta para que el profesor envíe los criterios de evaluación
@app.route('/submit_criteria', methods=['POST'])
def submit_criteria():
    data=request.json
    criteria = data.get('criteria')  # Criterios proporcionados por el profesor

    # Guardar los criterios en un archivo temporal
    with open(CRITERIA_FILE, 'w') as f:
        f.write(criteria)

    return jsonify({"message": "Criterios enviados con éxito. Procesando la revisión."})

# Función para ejecutar la IA una vez que ambos, ensayo y criterios, estén listos
@app.route('/process_evaluation', methods=['GET'])
def process_evaluation():
    # Verificar que tanto el ensayo como los criterios existan
    if not os.path.exists(ESSAY_FILE) or not os.path.exists(CRITERIA_FILE):
        return jsonify({"message": "Aún faltan datos. Asegúrate de que el estudiante haya enviado el ensayo y el profesor los criterios."})

    # Leer el ensayo y los criterios
    with open(ESSAY_FILE, 'r') as f:
        essay_text = f.read()

    with open(CRITERIA_FILE, 'r') as f:
        criteria = f.read()

    # Asignar el rol y construir los inputs para la IA
    role_text = "Usted es un asistente de redacción académica. Por favor, evalúe el ensayo centrándose en los siguientes aspectos y puntúe los ensayos de 0 a 10."
    system_instructions = f"{role_text} {criteria}"

    # Inputs para la IA
    inputs = [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": essay_text}
    ]

    # Ejecutar el modelo de IA (usando tu función `run_model`)
    result = run_model("@cf/meta/llama-3-8b-instruct", inputs, timeout=1200)
    print("Resultado de la IA:", result)

  # Revisar el resultado
    if 'error' in result:
        return jsonify({"message": "Error al procesar la solicitud: " + result['error']})

    try:
        # Verificar si 'result' y 'response' están presentes
        if 'result' in result and 'response' in result['result']:
            ai_response = result['result']['response']
            cleanText=TTS_GCP2.procesar_texto(ai_response)
            TTS_GCP2.run_and_save(cleanText,"cleanOutput.mp3")
            return jsonify({"message": "Revisión completada con éxito", "response": ai_response})
        else:
            # Si no está presente el campo esperado
            return jsonify({"message": "Error al procesar la respuesta de la IA: no se encontró 'response'."})
    except KeyError:
        return jsonify({"message": "Error al procesar la respuesta de la IA."})

    # Devolver la evaluación al cliente
# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

