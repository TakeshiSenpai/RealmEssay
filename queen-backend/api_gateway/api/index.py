import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from server_database.tareasdb_manager import TareasDBManager
tareas_db_manager = TareasDBManager()

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

@app.route('/get/tarea', methods=['POST'])
def get_tarea():
    code = request.json.get('code')
    email = request.json.get('email')
    tareas_db_manager.set_collection("Carpeta")

    carpetas = tareas_db_manager.read_all()
    tarea_encontrada = None
    carpeta_encontrada = None

    for carpeta in carpetas:
        for tarea in carpeta["data"]:
            if str(tarea["id"]) == code:
                for alumno in tarea["Alumnos"]:
                    print(alumno["email"])
                    if alumno["email"] == email:
                        alumno["Aceptada"] = True  
                        carpeta_encontrada = carpeta 
                        tarea_encontrada = tarea
                        break 

    tareas_db_manager.update_by_id(carpeta_encontrada["_id"], carpeta_encontrada)
    print(tarea_encontrada)

    return jsonify({'success': True, 'tarea': tarea_encontrada}), 200

@app.route('/get/tareas', methods=['POST'])
def get_tareas():
    email = request.json.get('email')
    tareas_db_manager.set_collection("Carpeta")
    carpetas = tareas_db_manager.read_all()
    carpetas_encontradas = []

    for carpeta in carpetas:
        for tarea in carpeta["data"]:
            for alumno in tarea["Alumnos"]:
                if alumno["email"] == email and alumno["Aceptada"]:
                    carpetas_encontradas.append(tarea)
    
    print(carpetas_encontradas)
    
    return jsonify({'success': True, 'tareas': carpetas_encontradas}), 200

@app.route('/get/tarea/id', methods=['POST'])
def get_tareas_id():
    # Validar que la solicitud tiene datos JSON válidos
    if not request.json or 'name' not in request.json:
        return jsonify({'success': False, 'error': 'Nombre de tarea no proporcionado'}), 400

    task_name = request.json.get('name')
    
    # Asegurarse de que `task_name` no sea None
    if not task_name:
        return jsonify({'success': False, 'error': 'Nombre de tarea vacío'}), 400
    
    tareas_db_manager.set_collection("Carpeta")
    carpetas = tareas_db_manager.read_all()
    tarea_encontrada = None

    try:
        # Extraer ID desde `task_name`
        id_tarea = task_name.split("-")[1].strip()  # Solo toma la primera parte y elimina espacios
        print(id_tarea)
        # Buscar la tarea correspondiente
        for carpeta in carpetas:
            for tarea in carpeta.get("data", []):  # Usa `.get()` para evitar errores si "data" no existe
                if str(tarea.get("id")) == id_tarea:
                    tarea_encontrada = tarea
                    break
            if tarea_encontrada:
                break  
        print(tarea_encontrada)
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al procesar la tarea: {str(e)}'}), 500

    if tarea_encontrada:
        return jsonify({'success': True, 'tarea': tarea_encontrada}), 200
    else:
        return jsonify({'success': False, 'error': 'Tarea no encontrada'}), 404

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2000)

