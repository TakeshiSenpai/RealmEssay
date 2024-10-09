import requests

# URL para procesar la evaluación
url = 'http://127.0.0.1:5000/process_evaluation'

# Realizar la solicitud GET al servidor Flask
response = requests.get(url)

# Imprimir la respuesta del servidor
print(response.json())

