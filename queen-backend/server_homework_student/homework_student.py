import io
import pdfplumber
from flask_cors import CORS
from flask import Flask,request,jsonify
import json

app = Flask(__name__)
CORS(app)

def extract_text_from_pdf(array_buffer):
    pdf_bytes = io.BytesIO(array_buffer)
    
    text = ""
    with pdfplumber.open(pdf_bytes) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    return text

# Ruta para enviar el ensayo y recibir la evaluación en fragmentos
@app.route('/submit_essay', methods=['POST'])
def submit_essay():

    pdf_data = request.data  

    pdf_bytes = io.BytesIO(pdf_data)
    text = ""
    with pdfplumber.open(pdf_bytes) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    data = {
        "input": text
    }

    with open('server_ia/ia_response/input.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    return jsonify({"message": "Todo correcto"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2004)