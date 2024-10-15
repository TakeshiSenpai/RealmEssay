import sys
import pathlib
from flask import Flask
from flask_cors import CORS

# Obtener la ruta al directorio raíz del proyecto (dos niveles hacia arriba)
root_dir = pathlib.Path(__file__).parent.parent.resolve()

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(str(root_dir))

# Importaciones absolutas ahora son posibles
from authentication import google_auth 
from ia_function.process_rubric.process_rubric import process_rubric

app = Flask(__name__)
CORS(app)

@app.route('/login/google', methods=['POST'])
def login_google():
    return google_auth.login_google()

@app.route('/tarea/rubrica', methods=['POST'])
def get_rubric():
    return process_rubric()

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(port=5000)
