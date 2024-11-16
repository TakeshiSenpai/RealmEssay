import pathlib
import os
from os.path import dirname, abspath, join
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
try:
    #En vercel asi deberia ser porque el root es server_ia
    from ia_response import ia_response
except:
    from  server_ia.ia_response import ia_response

#El de welcome esta hecho para probar como funciona el vercel



@app.route('/api', methods=['GET'])
def welcome():
    return jsonify({'success':True, 'message':'welcome ia... uhm, i think is better to say: welcome developer'}),200



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
        def stream_response():
            for fragment in ia_response.process_questions_and_responses(student_questions):
                yield fragment

        # Retornar el stream usando la función generadora
        return Response(stream_response(), content_type='text/event-stream')

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

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

@app.route('/write_input', methods=['POST'])
def write_input():
    print(os.getcwd())
    os.path.join("/tmp","input.json")
    mensaje= ""
    try:
        if "VERCEL_ENV" in os.environ:  # Esta variable solo existe en Vercel
            file_path = '/tmp/input.json'
            mensaje="Si leyo el vercel_ENV"
            print(mensaje)
        else:
            file_path = 'server_ia/ia_response/input.json'
            mensaje = "No lo leyo el vercel_ENV"
            print(mensaje)

        data = request.json.get('data')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return jsonify({"message": f"Texto guardado exitosamente, {mensaje}"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al enviar los criterios: {str(e)} , {mensaje}"}), 400
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2003)