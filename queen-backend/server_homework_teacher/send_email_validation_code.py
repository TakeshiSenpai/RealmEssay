import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from flask import request, jsonify

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Esta función envía un correo electrónico a los alumnos con un código de validación.
# Los alumnos deberán ingresar este código para poder enviar la tarea.
def send_email_validation_code():
    try:
        # Obtener los datos de la solicitud
        html = request.json.get('html')  # El contenido HTML del correo
        email_to = request.json.get('to')  # Lista de correos electrónicos de los alumnos
        password = os.getenv('PASS')  # Contraseña del correo desde el archivo .env
        email_from = "realmessay@gmail.com"  # Correo del remitente

        mensaje_de_regreso = ""

        # Conectar al servidor SMTP de Gmail para enviar el correo
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Usar una conexión segura
        server.login(email_from, password)  # Iniciar sesión con el correo del remitente

        # Verificar si el contenido HTML está vacío
        if not html:
            return jsonify({'success': False, 'message': 'El contenido HTML está vacío'}), 400

        # Enviar el correo a cada destinatario
        for to in email_to:
            try:
                # Crear el mensaje MIME
                msg = MIMEMultipart()
                msg['Subject'] = "Código de envío de ensayo"  # Asunto del correo
                msg['From'] = email_from
                msg['To'] = to

                # Adjuntar el contenido HTML al mensaje
                msg.attach(MIMEText(html, 'html'))

                # Enviar el correo
                server.sendmail(email_from, to, msg.as_string())
                mensaje_de_regreso += "Mensaje enviado a " + to + ", "
            except Exception as e:
                mensaje_de_regreso += f"Error al enviar a {to}: {str(e)}, "
                continue

        # Cerrar la conexión con el servidor SMTP
        server.quit()

        # Retornar el mensaje de éxito con los destinatarios a los que se les envió el correo
        return jsonify({'success': True, 'message': mensaje_de_regreso}), 200

    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error
        return jsonify({'success': False, 'message': f'Ocurrió un error: {str(e)}'}), 400
