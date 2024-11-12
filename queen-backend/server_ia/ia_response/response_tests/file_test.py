import re
import sys

import pathlib
import requests
from pypdf import PdfReader

# Agregar el directorio raíz al sys.path para importar módulos
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.resolve()))

def getPDFText(file):
    pdf = PdfReader(file)
    text = ''
    for page in pdf.pages:
        pageText = ' '.join(page.extract_text().splitlines())
        text += pageText + ' '
    return text

# URLs del servidor
url = 'http://127.0.0.1:2003/submit_essay'
url_force_evaluation = 'http://127.0.0.1:2003/force_evaluation'

def clean_text(text):
    """Limpia el texto del ensayo eliminando caracteres innecesarios."""
    text = text.replace('\t', ' ')
    cleaned_text = re.sub(r'●\s*', '', text)  # Elimina "● Se" y espacios extras
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Reemplaza múltiples espacios por uno solo
    return cleaned_text.strip()  # Elimina espacios al inicio y al final

def real_input(data):
    #Envía el ensayo al servidor y, si es necesario, recurre a force_evaluation.
    # Intentar primero la URL de `submit_essay`
    response = requests.post(url, json=data, stream=True)
    
    def process_stream(response):
        print("Respuesta del servidor en fragmentos:")
        for chunk in response.iter_lines():
            if chunk:
                decoded_chunk = chunk.decode('utf-8')
                if decoded_chunk == "[DONE]":
                    print("Transmisión completada.")
                    return True
                print(decoded_chunk)
        return False

    if response.status_code == 200 and process_stream(response):
        print("Evaluación completada con submit_essay.")
    

# Función principal que combina la limpieza y envío del ensayo
def test(filename):
    text = getPDFText(filename)
    text = clean_text(text)
    text_data = {'essay': text}
    
    # Enviar el ensayo al servidor
    real_input(text_data)
    #print(text_data)

test(str(pathlib.Path('Propuesta de arquitectura.pdf').resolve()))
