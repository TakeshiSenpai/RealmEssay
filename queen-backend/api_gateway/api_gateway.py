from flask import Flask,request,jsonify
from flask_cors import CORS
import pathlib,sys
# Importaciones absolutas ahora son posibles
from authentication import google_auth 
current_file=pathlib.Path(__file__)
parent_dir=current_file.parent.parent
#print(str(parent_dir))
sys.path.append(str(parent_dir))
from ia_function.ia_response import ia_response
app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    return google_auth.login_google()

@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    pass
    #return process_rubric()

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
        result = ia_response.process_response()
        return jsonify({"response": result}), 200
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

if __name__ == '__main__':
    app.run(debug=True)
