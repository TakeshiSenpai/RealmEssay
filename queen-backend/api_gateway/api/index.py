import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para iniciar sesión con Google
@app.route('/login/google', methods=['POST'])
def login_google():
    google_token = request.json.get('token')
    response = requests.post("http://127.0.0.1:2001/login/google", json={"token": google_token})
    return jsonify(response.json()), 200 
@app.route('/api', methods=['GET'])
def welcome():
    return jsonify({'success':True, 'message':'welcome to api gateway'}),200

# Ruta para enviar el código de validación por correo electrónico
@app.route('/tarea/email/code', methods = ['POST'])
def send_email():
    rubrica = request.json.get('rubrica')
    response = requests.post("http://127.0.0.1:2002/tarea/email/code", json={"rubrica": rubrica})

    return jsonify(response.json()), 200 

# Ruta para obtener la rúbrica de la tarea
@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    rubrica = request.json.get('rubrica')
    response = requests.post("http://127.0.0.1:2003/tarea/rubrica", json={"rubrica": rubrica})

    return jsonify(response.json()), 200 

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run()

