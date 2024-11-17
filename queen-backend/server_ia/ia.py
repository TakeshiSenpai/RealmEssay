from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from ia_response import ia_response_claude as ia_response
import json

app = Flask(__name__)
CORS(app)

# Ruta para procesar la rúbrica de la tarea
@app.route('/tarea/rubrica', methods=['POST'])
def process_rubric():
    rubric = request.json.get('rubrica')

    if rubric is None:
        return jsonify({'success': False, 'message': 'Rúbrica no recibida'}), 400

    message = (
        "Se te presenta la rúbrica para evaluar el ensayo. Consta de "
        + str(len(rubric))
        + " parámetros, cada uno con un título, descripción, valor máximo y un conjunto de niveles de desempeño (criterios)."
        + " Cada nivel tiene una descripción y un puntaje asociado."
        + " Selecciona el nivel de desempeño más adecuado para cada parámetro del ensayo."
        + " Al final, deberás presentar el puntaje total, indicando el puntaje de cada parámetro y proporcionando una breve justificación."
    )

    for index, parameter in enumerate(rubric):
        message += (
            f"\n\nParámetro {index + 1}: {parameter['title']}"
        )

        if parameter.get('description'):
            message += f"\nDescripción: {parameter['description']}"

        message += f"\nValor total: {parameter['totalValue']}\nCriterios:"

        for criteria_index, criteria in enumerate(parameter['criterias']):
            message += (
                f"\n\tCriterio {criteria_index + 1}: {criteria['description']}"
                f"\n\tValor parcial: {criteria['partialValue']}"
            )

    return jsonify({'success': True, 'message': message}), 200

# Ruta para obtener la respuesta de la IA al momento de realizar preguntas sobre la evaluación (streaming en tiempo real)
@app.route('/questions_and_responses', methods=['POST'])
def get_response():
    try:
        #student_questions del cuerpo de la solicitud POST
        data = request.json
        student_questions = data.get("student_questions", [])
        # Procesar la respuesta como un stream de datos
        def generate():
            for chunk in ia_response.process_questions_and_responses(data):
                if isinstance(chunk, str):
                    yield f"data: {json.dumps({'text': chunk})}\n\n"
                else:
                    yield f"data: {json.dumps(chunk)}\n\n"

        # Retornar el stream usando la función generadora
        return Response(generate(), content_type='text/event-stream')

    except Exception as e:
        return jsonify({"error": f"Error al obtener la respuesta: {str(e)}"}), 500

# Ruta para enviar los criterios de la IA
@app.route('/submit_criteria', methods=['POST'])
def submit_criteria():
    try:
        criteria_data = request.json
        ia_response.submit_criteria(criteria_data)
        return jsonify({"message": "Criterios enviados exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al enviar los criterios: {str(e)}"}), 500


@app.route('/submit_essay', methods=['POST'])
def handle_submit_essay():
    try:
        data = request.get_json()
        if not data or 'input' not in data:
            return jsonify({"error": "No essay provided"}), 400

        def generate():
            for chunk in ia_response.submit_essay(data):
                if isinstance(chunk, str):
                    yield f"data: {json.dumps({'text': chunk})}\n\n"
                else:
                    yield f"data: {json.dumps(chunk)}\n\n"

        return Response(generate(), mimetype='text/event-stream')
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2003)