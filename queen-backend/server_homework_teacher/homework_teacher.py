from logging import exception
from textwrap import indent

from flask import Flask,request,jsonify
from flask_cors import CORS
from flask.cli import load_dotenv
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask.cli import load_dotenv

#Librerias para la base de datos
from pymongo import MongoClient
from bson.objectid import ObjectId

#Lo de la base de datos
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
tarea_collection = db["Tarea"]

import json
app = Flask(__name__)
CORS(app)

@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response
    
@app.route('/tarea/email/code', methods=['POST'])
def send_email_validation_code():
     try:
         load_dotenv()

         html = request.json.get('html')
         email_to = request.json.get('to')
         subject = request.json.get('subject')
         password = os.getenv('PASS') #debe ir en un env, pero de momento no lo haré xd si lo hice
         email_from = "realmessay@gmail.com"
         mensaje_de_regreso = ""
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login(email_from, password)

         if html =="":
             return jsonify({'success': False, 'message': 'Se envio mal el html'}), 400

         for to in email_to:
             try:
                 msg =MIMEMultipart()
                 msg['Subject'] = subject
                 msg['From'] = email_from
                 msg['To'] = to

                 #Adjuntar contenido de html es decir la plantilla
                 msg.attach(MIMEText(html,'html'))
                 #Enviar correo
                 server.sendmail(
                     email_from,
                     to,
                     msg.as_string()
                 )
                 mensaje_de_regreso = mensaje_de_regreso+"mensaje enviado, "
             except:
                 mensaje_de_regreso=mensaje_de_regreso+"Destinatario no encontrado, "
                 continue
         #Se cierra la conexion
         server.quit()
         return jsonify({'success': True, 'message': mensaje_de_regreso}), 200
     except Exception as e:
        return jsonify({'success': False, 'message': f'Ocurrio algún error: {str(e)}'}), 400

#Explicacion del json
#-Nombre de Tarea es un string
#-Rubrica es un string enorme
#-Alumnos es un arreglo de string en donde solo estara el email
#-Descripcion

@app.route('/tarea/postDB', methods=['POST'])
def post_tarea_db():
    try:
        profesor = request.json.get('Profesor')
        nombre = request.json.get('Nombre')
        rubrica = request.json.get('Rubrica')
        alumnos = request.json.get('Alumnos')
        descripcion = request.json.get('Descripcion')
        id = request.json.get("id")
        datos_tarea = {
            "id":id,
            "Profesor": profesor,
            "Descripcion": descripcion,
            "Nombre": nombre,
            "Rubrica": rubrica,
            "Alumnos": alumnos
        }
        # Insertar la tarea en la colección
        tarea_collection.insert_one(datos_tarea)
        #print(f"Tarea creada con ID: {resultado.inserted_id}")

        return jsonify({'success': True, 'message': 'Tarea guardada'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error{str(e)}'}), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2002)