import base64
import io
import json
import pdfplumber
import requests
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import os
from flask_cors import cross_origin
app = Flask(__name__)
CORS(app)
#El de welcome esta hecho para probar como funciona el vercel

ia_server_url = os.getenv("VERCEL_IA","127.0.0.1:2003")
ia_server_url = f"https://{ia_server_url}" if "VERCEL_IA" in os.environ else f"http://{ia_server_url}"
@app.route('/api', methods=['GET'])
def welcome():
    return jsonify({'success':True, 'message':'welcome student'}),200

def extract_text_from_pdf(array_buffer):
    pdf_bytes = io.BytesIO(array_buffer)
    
    text = ""
    with pdfplumber.open(pdf_bytes) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    return text

# Ruta para obtener el ensayo en formato PDF o TXT, extraer el texto y guardarlo en el input.json
@app.route('/submit_essay', methods=['POST'])
def submit_essay():
    file_name = request.json.get('fileName').lower()
    file_data = request.json.get('fileData')

    if not file_name or not file_data:
        return jsonify({"message": "No se pudo encontrar los datos del archivo."}), 400

    if file_name.endswith('.pdf'):
        try:
            pdf_bytes = io.BytesIO(base64.b64decode(file_data))
            text = ""

            with pdfplumber.open(pdf_bytes) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""

            data = {
                "input": text
            }
            auth_data = {'data': data}
            resp = requests.post(f"{ia_server_url}/write_input", json=auth_data)
            if resp.status_code == 200:  # Buen post
                return Response(status=200)
            else:
                return jsonify({"message": f"Error al intentar comunicarse con ia_server."}), 500

        except Exception as e:
            return  jsonify({"message": f"Error interno al decodificar el archivo PDF. ERROR {e}"}), 500

    elif file_name.endswith('.txt'):
        try:

            data = {
                "input": base64.b64decode(file_data).decode('utf-8')
            }
            auth_data = {'data':data}
            resp = requests.post(f"{ia_server_url}/write_input",json=auth_data)
            if resp.status_code == 200:#Buen post
                return Response(status=200)
            else:
                return jsonify({"message": f"Error al intentar comunicarse con ia_server."}), 400
        except Exception as e:
            return jsonify({"message": f" Error interno al decodificar el archivo TXT. ERROR {e}"}),400

    else:
        return jsonify({"message": "Formato de archivo no soportado."}), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2004)