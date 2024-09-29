import requests

# URL para enviar el ensayo
url = 'http://127.0.0.1:5000/submit_essay'

# Datos a enviar
data = {
    'essay': 'Este es el ensayo del estudiante que será evaluado.'
}

# Enviar la solicitud POST al servidor Flask
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.json())
