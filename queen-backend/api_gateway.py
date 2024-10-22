import pathlib
import requests
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

current_file=pathlib.Path(__file__)
parent_dir=current_file.parent.parent
sys.path.append(str(parent_dir))

app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    google_token = request.json.get('token')
    response = requests.post("http://127.0.0.1:2001/login/google", json={"token": google_token})
    return jsonify(response.json()), 200 

@app.route('/tarea/email/code', methods = ['POST'])
def send_email():
    rubrica = request.json.get('rubrica')
    response = requests.post("http://127.0.0.1:2002/tarea/email/code", json={"rubrica": rubrica})

    return jsonify(response.json()), 200 

@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    rubrica = request.json.get('rubrica')
    response = requests.post("http://127.0.0.1:2003/tarea/rubrica", json={"rubrica": rubrica})

    return jsonify(response.json()), 200 



"""
# Ruta para enviar datos de la IA
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        # Enviamos los datos a la función submit() de ia_response
        result = ia_response.submit(data)
        return jsonify({"message": "Datos procesados exitosamente", "result": result}), 200
    except Exception as e:
        return jsonify({"error": f"Error al procesar los datos: {str(e)}"}), 500


# Ruta para obtener la respuesta de la IA
@app.route('/response', methods=['GET'])
def get_response():
    try:
        # Procesar la respuesta como un stream de datos
        def stream_response():
            for fragment in ia_response.process_response():
                yield f"data: {fragment}\n\n"  # Enviar cada fragmento al cliente progresivamente
                import sys
                sys.stdout.flush()  # Asegurarnos de que se "flushee" el buffer

        # Retornamos el stream usando la función generadora
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

"""

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2000)

