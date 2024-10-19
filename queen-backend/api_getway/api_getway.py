from flask import Flask
from flask_cors import CORS

import authentication.google_auth as google_auth
from ia_function.process_rubric.process_rubric import process_rubric
from send_emails.send_email_validation_code import send_email_validation_code

app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    return google_auth.login_google()

@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    return process_rubric()
@app.route('/tarea/email/code', methods = ['POST'])
def send_email():
    return send_email_validation_code()


@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(port=5000)