from flask import Flask
from flask_cors import CORS
import Auth.google_auth as google_auth

app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    return google_auth.login_google()

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(port=5000)