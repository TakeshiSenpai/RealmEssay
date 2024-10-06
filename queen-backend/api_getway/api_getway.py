from flask import Flask, jsonify, request
from flask_cors import CORS

import Auth.google_auth as google_auth

app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    return google_auth.login_google()

@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    if request.json.get('rubrica'):
        print(request.json.get('rubrica'))
        return jsonify({'success': True, 'message': 'Rúbrica recibida'}), 200
    else:
        return jsonify({'success': False, 'message': 'Rúbrica no recibida'}), 400

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(port=5000)