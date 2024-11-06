import base64
import io
import json

import pdfplumber
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

            with open('server_ia/ia_response/input.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                return Response(status=200)
        except:
            return jsonify({"message": f"Error interno al extraer el texto del archivo PDF."}), 500

    elif file_name.endswith('.txt'):
        try:
            data = {
                "input": base64.b64decode(file_data).decode('utf-8')
            }

            with open('server_ia/ia_response/input.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                return Response(status=200)
        except:
            return jsonify({"message": f"Error interno al decodificar el archivo TXT."}), 500

    else:
        return jsonify({"message": "Formato de archivo no soportado."}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2004)