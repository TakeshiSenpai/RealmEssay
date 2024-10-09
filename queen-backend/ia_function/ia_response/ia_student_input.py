import requests

# URL para enviar el ensayo
url = 'http://127.0.0.1:5000/submit_essay'


def real_input(data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        # Imprimir la respuesta del servidor
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"error al realizar la solicitud {e}")



def test_input():
    # Datos a enviar
    data = {
        'essay': 'El automovilismo deportivo ha experimentado una evolución impresionante desde sus inicios a finales del siglo XIX. Lo que comenzó como simples carreras entre automóviles para demostrar la viabilidad del motor de combustión interna, ha evolucionado hasta convertirse en una de las disciplinas más tecnológicas y desafiantes del deporte mundial.En sus primeros años, las competiciones eran caóticas y a menudo peligrosas. Los pilotos competían en caminos de tierra, sin las medidas de seguridad que hoy consideramos esenciales. Con el tiempo, los avances en ingeniería automotriz y las mejoras en las pistas de carreras ayudaron a reducir los riesgos y a hacer que el deporte fuera más atractivo tanto para los pilotos como para los espectadores..'
    }

    # Enviar la solicitud POST al servidor Flask
    response = requests.post(url, json=data)

    # Imprimir la respuesta del servidor
    print(response.json())


test_input()