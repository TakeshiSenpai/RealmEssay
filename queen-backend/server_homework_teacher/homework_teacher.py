import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
# Librerías para conexión a la base de datos MongoDB
from pymongo import MongoClient

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Conexión a la base de datos MongoDB
client = MongoClient(
    "mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
tarea_collection = db["Tarea"]

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde otros dominios


@app.after_request
def add_header(response):
    """
    Se ejecuta después de cada solicitud para agregar los encabezados de seguridad.
    """
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response


@app.route('/tarea/email/code', methods=['POST'])
def send_email_validation_code():
    """
    Enviar un correo electrónico de validación con un código HTML a los destinatarios especificados.
    """
    try:
        # Cargar las variables de entorno del archivo .env
        html = request.json.get('html')  # Contenido HTML del correo
        email_to = request.json.get('to')  # Lista de correos a los que se enviará el mensaje
        subject = request.json.get('subject')  # Asunto del correo
        password = os.getenv('PASS')  # Contraseña del correo desde el archivo .env
        email_from = "realmessay@gmail.com"  # Correo del remitente

        if not html:
            # Validación de contenido HTML vacío
            return jsonify({'success': False, 'message': 'El contenido HTML está vacío'}), 400

        # Conectar al servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_from, password)

        mensaje_de_regreso = ""
        # Enviar correos a cada destinatario en la lista
        for to in email_to:
            try:
                # Crear el mensaje MIME
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = email_from
                msg['To'] = to
                msg.attach(MIMEText(html, 'html'))  # Adjuntar contenido HTML al correo

                # Enviar el correo
                server.sendmail(email_from, to, msg.as_string())
                mensaje_de_regreso += "Mensaje enviado, "
            except Exception as e:
                mensaje_de_regreso += f"Error al enviar a {to}: {str(e)}, "
                continue

        # Cerrar la conexión con el servidor SMTP
        server.quit()
        return jsonify({'success': True, 'message': mensaje_de_regreso}), 200

    except Exception as e:
        return jsonify({'success': False, 'message': f'Ocurrió un error: {str(e)}'}), 400


@app.route('/tarea/postDB', methods=['POST'])
def post_tarea_db():
    """
    Guardar una nueva tarea en la base de datos MongoDB.
    """
    try:
        # Obtener los datos de la tarea del cuerpo de la solicitud
        profesor = request.json.get('Profesor')
        nombre = request.json.get('Nombre')
        rubrica = request.json.get('Rubrica')
        alumnos = request.json.get('Alumnos')
        descripcion = request.json.get('Descripcion')
        tarea_id = request.json.get("id")  # ID único para la tarea (puede generarse automáticamente)

        # Crear el diccionario con los datos de la tarea
        datos_tarea = {
            "id": tarea_id,
            "Profesor": profesor,
            "Descripcion": descripcion,
            "Nombre": nombre,
            "Rubrica": rubrica,
            "Alumnos": alumnos
        }

        # Insertar la tarea en la base de datos
        tarea_collection.insert_one(datos_tarea)
        return jsonify({'success': True, 'message': 'Tarea guardada correctamente'}), 200

    except Exception as e:
        return jsonify({'success': False, 'message': f'Error al guardar la tarea: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2002)