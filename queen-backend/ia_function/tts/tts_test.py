import tts_local

def run_and_save_from_file(file_path):
    """Read text from a file and convert it to a voice file"""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            print(f"Text read from file: {text}")
            
            if text.strip():  # Verifica que el archivo no esté vacío
                tts_local.run_and_save(text)  # Llama a la función para guardar el audio
                print("Audio generation started.")
            else:
                print("The file is empty or contains only whitespace.")
    except Exception as e:
        print(f"An error occurred: {e}")

run_and_save_from_file("../ia_response/test.txt")
