import AI_StudentInput
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
    AI_StudentInput.realInput(text_data)

test('queen-backend\\Func_AI\\get_essay_text\\Propuesta de arquitectura.pdf')


