import requests

# URL para procesar la evaluación
url = 'http://127.0.0.1:5000/response'

# Hacer la solicitud GET con la opción de 'stream' habilitada
response = requests.get(url, stream=True)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print("Recibiendo la respuesta en fragmentos:")
    
    # Leer los fragmentos a medida que se reciben
    for chunk in response.iter_lines():
        if chunk:
            # Decodificar y procesar cada fragmento de datos
            decoded_chunk = chunk.decode('utf-8')
            if decoded_chunk == "[DONE]":
                print("Stream completado.")
                break
            print(decoded_chunk)
else:
    print(f"Error: {response.status_code} - {response.text}")
