import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Rutas donde se almacenarán temporalmente los datos
ESSAY_FILE = "essay.txt"
CRITERIA_FILE = "criteria.txt"

# Ruta para que el estudiante envíe el ensayo
@app.route('/submit_essay', methods=['POST'])
def submit_essay():
    essay_text = request.form['essay']  # Obtenemos el texto enviado por el estudiante

    # Guardar el ensayo en un archivo temporal
    with open(ESSAY_FILE, 'w') as f:
        f.write(essay_text)

    return jsonify({"message": "Ensayo enviado con éxito. Esperando criterios del profesor."})

# Ruta para que el profesor envíe los criterios de evaluación
@app.route('/submit_criteria', methods=['POST'])
def submit_criteria():
    criteria = request.form['criteria']  # Criterios proporcionados por el profesor

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
    role_text = "You are an academic writing assistant. Please evaluate the essay focusing on the following aspects."
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
        ai_response = result['content']
    except KeyError:
        return jsonify({"message": "Error al procesar la respuesta de la IA."})

    # Devolver la evaluación al cliente
    return jsonify({"message": "Revisión completada con éxito", "response": ai_response})
