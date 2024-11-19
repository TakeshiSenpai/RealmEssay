import datetime
import jwt
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.auth.transport import requests
from google.oauth2 import id_token
from server_database.tareasdb_manager import TareasDBManager
from server_database.chatdb_manager import ChatDBManager

app = Flask(__name__)
CORS(app)

chat_db_manager = ChatDBManager()
tareas_db_manager = TareasDBManager()

# Client ID de Google
GOOGLE_CLIENT_ID = "496696206304-fsqr77k8ao63rv6tuskh5lu4ph5p4fo3.apps.googleusercontent.com"

# Clave secreta para firmar los JWT
SECRET_KEY = 'The princesses are the best' 

def generate_jwt(user_info):
    payload = {
        'sub': user_info['email'],  
        'name': user_info['name'],
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

@app.route('/api', methods=['GET'])
def welcome():
    return jsonify({'success':True, 'message':'Welcome to authentication server'}),200

@app.route('/login/google', methods=['POST'])
def login_google():
    token = request.json.get('token')
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        user_info = {
            'name': idinfo.get('name'),
            'email': idinfo.get('email'),
            'picture': idinfo.get('picture'),
        }
        jwt_token = generate_jwt(user_info)

        chat_db_manager.set_collection("Carpeta")
        tareas_db_manager.set_collection("Carpeta")

        carpetas = chat_db_manager.read_all()
        existe_correo = any(carpeta.get('email') == idinfo.get("email") for carpeta in carpetas)

        if not existe_correo:
            carpeta = {
                "nombre": idinfo.get("name"),
                "email": idinfo.get("email"),
                "data": []
            }
            chat_db_manager.create_from_json_object(carpeta)
            tareas_db_manager.create_from_json_object(carpeta)

        return jsonify({'success': True, 'user_info': user_info, 'token': jwt_token}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Invalid token {e}'}), 400
    
@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2001)
