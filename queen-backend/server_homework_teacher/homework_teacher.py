from flask import Flask,request,jsonify
from flask_cors import CORS
from flask.cli import load_dotenv
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask.cli import load_dotenv


app = Flask(__name__)
CORS(app)

@app.route('/tarea/email/code', methods=['POST'])
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
    
@app.after_request
def add_header(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2002)