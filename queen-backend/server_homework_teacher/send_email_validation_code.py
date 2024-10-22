#Aqui se va a enviar el email a los alumnos diciendo que deben colocar el codigo para
#poder enviar la tarea
import smtplib
import os
from dotenv import load_dotenv
from warnings import catch_warnings

from flask import request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask.cli import load_dotenv


def send_email_validation_code():
    try:
        load_dotenv()

        html = request.json.get('html')
        email_to = request.json.get('to')
        password = os.getenv('PASS') #debe ir en un env, pero de momento no lo haré
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
                msg['Subject'] = "Código de enivío de ensayo"
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


