import requests,time

# URL para procesar la evaluación
url = 'http://127.0.0.1:2003/questions_and_responses'

# Datos que se enviarán en la solicitud POST
data = {
    "student_questions": [
        "¿Qué puedo mejorar en la argumentacion?"
    ]
}
inicio=time.time()
# Hacer la solicitud POST con stream habilitado
response = requests.post(url, json=data, stream=True)

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
            print("Fragmento recibido:", decoded_chunk)
else:
    print(f"Error: {response.status_code} - {response.text}")
final=time.time()
tiempo_exec=final-inicio
print(f"tiempo de ejecucion {tiempo_exec} seg")