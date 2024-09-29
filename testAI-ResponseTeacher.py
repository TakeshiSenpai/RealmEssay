import requests

# URL para enviar los criterios
url = 'http://127.0.0.1:5000/submit_criteria'

# Datos a enviar
data = {
    'criteria': 'Grammar, Structure, Argumentation'
}

# Enviar la solicitud POST al servidor Flask
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.json())
