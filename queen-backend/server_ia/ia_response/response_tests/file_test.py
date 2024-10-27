from pathlib import Path

import ia_student_input
from get_essay_text import get_essay_text

import re

def clean_text(text):
    # Eliminar "● Se" y cualquier otro texto similar
    text = text.replace('\t', ' ')
    cleaned_text = re.sub(r'●\s*', '', text)  # Elimina "● Se" seguido de cualquier espacio
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Reemplaza múltiples espacios por uno solo
    return cleaned_text.strip()  # Eliminar espacios al inicio y al final

# Ejemplo de uso
def test(filename):
    text=get_essay_text.getPDFText(filename)
    text=clean_text(text)
    #print(text)
    text_data={
        'essay' : text
    }
    print(text_data)
    ia_student_input.real_input(text_data)

test(str(Path('../get_essay_text/Propuesta de arquitectura.pdf')))
