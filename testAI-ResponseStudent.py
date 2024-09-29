import requests

# Define la URL del endpoint de Flask
url = 'http://127.0.0.1:5000/submit'

# El texto del ensayo que queremos enviar
data = {
    'essay': 'Este es un ensayo de prueba para revisar.'
}

# Enviar la solicitud POST al servidor Flask
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response)
