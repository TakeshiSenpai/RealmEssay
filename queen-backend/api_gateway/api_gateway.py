from flask import Flask
from flask_cors import CORS
import pathlib,sys
# Importaciones absolutas ahora son posibles
from authentication import google_auth 
current_file=pathlib.Path(__file__)
parent_dir=current_file.parent.parent
print(str(parent_dir))
sys.path.append(str(parent_dir))
from ia_function.ia_response import ia_response
ia_response.run
app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    return google_auth.login_google()

@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    pass
    #return process_rubric()

@app.route('/submit',methods=['POST'])
def submit():
    return

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(debug=True)
