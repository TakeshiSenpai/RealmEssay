import requests

# URL para enviar el ensayo
url = 'http://127.0.0.1:2003/submit_essay'


def real_input(data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        # Imprimir la respuesta del servidor
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"error al realizar la solicitud {e}")

def test_input():
    data = {
        'input': 'El automovilismo deportivo ha experimentado una evolución impresionante desde sus inicios a finales del siglo XIX. Lo que comenzó como simples carreras entre automóviles para demostrar la viabilidad del motor de combustión interna, ha evolucionado hasta convertirse en una de las disciplinas más tecnológicas y desafiantes del deporte mundial.En sus primeros años, las competiciones eran caóticas y a menudo peligrosas. Los pilotos competían en caminos de tierra, sin las medidas de seguridad que hoy consideramos esenciales. Con el tiempo, los avances en ingeniería automotriz y las mejoras en las pistas de carreras ayudaron a reducir los riesgos y a hacer que el deporte fuera más atractivo tanto para los pilotos como para los espectadores..'
    }

    # Enviar la solicitud POST al servidor con `stream=True`
    response = requests.post(url, json=data, stream=True)

    # Verificar si la respuesta es exitosa
    if response.status_code == 200:
        print("Respuesta del servidor en fragmentos:")
        for chunk in response.iter_lines():
            if chunk:
                decoded_chunk = chunk.decode('utf-8')
                if decoded_chunk == "[DONE]":
                    print("Transmisión completada.")
                    break
                print(decoded_chunk)
    else:
        print(f"Error {response.status_code}: {response.text}")

# Ejecutar la función de prueba
test_input()

