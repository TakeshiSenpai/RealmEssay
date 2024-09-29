import re
from google.cloud import texttospeech
import os

# Configura el entorno con la ruta de las credenciales
os.environ["GOOGLE_APP_CREDENTIALS"]="auth/testservices-437021-9f204df463fb.json"

# Función para limpiar el texto
def procesar_texto(texto):
    # Eliminar asteriscos
    texto_limpio = texto.replace('*', '')
    
    # Reemplazar dobles saltos de línea con una pausa larga (marcada como un punto y seguido)
    texto_limpio = texto_limpio.replace('\n\n', '. ')

    # Reemplazar saltos de línea simples con una pausa corta (una coma o simplemente un espacio)
    texto_limpio = texto_limpio.replace('\n', ', ')
    
    return texto_limpio



# Función para convertir el texto en audio usando la API de Google
def run_and_save(text, output_filename):
    # Crea un cliente
    client = texttospeech.TextToSpeechClient()

    # Configura el input de la síntesis con el texto procesado
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice=texttospeech.VoiceSelectionParams(
        language_code="es-US",
        name="es-US-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    # Configura el formato de salida
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # Guardar en formato MP3
    )

    # Realiza la solicitud a la API para convertir el texto a voz
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Guarda la respuesta como un archivo de audio
    with open(output_filename, "wb") as out:
        # Escribe el audio al archivo
        out.write(response.audio_content)
        print(f'Audio guardado como {output_filename}')

# Convertir el texto procesado a audio
#run_and_save(texto_procesado, "evaluacion_ensayo_limpio.mp3")