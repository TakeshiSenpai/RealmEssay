import requests

# URL para enviar los criterios
url = 'http://127.0.0.1:5000/submit_criteria'


def realInput(data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        # Imprimir la respuesta del servidor
        print(response.json())
    except requests.exceptions.requestException as e:
        print("error al realizar la solicitud {e}")


def testInput():
    # Datos a enviar
    data = {
        'criteria': 'Gramática, estructura y argumentación'
    }

    # Enviar la solicitud POST al servidor Flask
    response = requests.post(url, json=data)

    # Imprimir la respuesta del servidor
    print(response.json())


testInput()