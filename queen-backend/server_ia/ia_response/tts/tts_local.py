import subprocess


# Función para limpiar el texto
def procesar_texto(texto):
    """
    Limpia el texto para adaptarlo al formato esperado por el TTS.

    - Elimina asteriscos.
    - Reemplaza dobles saltos de línea por puntos y seguidos.
    - Reemplaza saltos de línea simples por comas.

    Args:
        texto (str): Texto de entrada a procesar.

    Returns:
        str: Texto limpio.
    """
    # Eliminar asteriscos
    texto_limpio = texto.replace('*', '')

    # Reemplazar dobles saltos de línea con una pausa larga
    texto_limpio = texto_limpio.replace('\n\n', '. ')

    # Reemplazar saltos de línea simples con una pausa corta
    texto_limpio = texto_limpio.replace('\n', ', ')

    return texto_limpio


# Función para ejecutar edge_tts
def run_edge_tts(text, voice):
    """
    Ejecuta el comando edge_tts con el texto y la voz proporcionados.

    Args:
        text (str): Texto a convertir en audio.
        voice (str): Nombre de la voz a utilizar en edge_tts.

    Raises:
        subprocess.CalledProcessError: Si el comando falla.
    """
    clean_text = procesar_texto(text)
    command = f"edge-tts --voice {voice} --text \"{clean_text}\" --write-media cleanOutput.mp3 --write-subtitles cleanOutput.vtt"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Audio generado con éxito: cleanOutput.mp3")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar edge_tts: {e}")


