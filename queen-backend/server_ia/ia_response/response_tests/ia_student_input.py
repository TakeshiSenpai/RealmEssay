import requests

# URL para enviar el ensayo
url = 'http://127.0.0.1:2003/submit_essay'

        
def test_input():
    data = {
        'input': "Universidad Aut\u00f3noma de Baja California Ingenier\u00eda en computaci\u00f3n Realm Essay - Propuesta de arquitectura Dur\u00e1n C\u00e1rdenas H\u00e9ctor Jes\u00fas 1176461 Gonz\u00e1lez Tiang Al\u00e1n Antonio 1170228 Larra\u00f1aga Flores Luis Leonardo 1183087 N\u00fa\u00f1ez L\u00f3pez Luis Manuel 1182533 P\u00e9rez Solorio Kadir Josafat 1182567 Ingenier\u00eda de Software Prof. Jos\u00e9 Mart\u00edn Olgu\u00edn Espinoza 2024, Mexicali B.C. \u00cdndice 1. Introducci\u00f3n 3 1.1 Prop\u00f3sito 3 1.2 Alcance 3 1.3 Definiciones, Acr\u00f3nimos y Abreviaturas 3 2. Representaci\u00f3n Arquitect\u00f3nica 3 3. Objetivos Arquitect\u00f3nicos y Restricciones 5 3.1 Objetivos 5 3.2 Restricciones 5 4. Vista de casos de uso 5 5. Vista de Componentes 6 7. Tama\u00f1o y desempe\u00f1o 7 8. Calidad 7 1. Introducci\u00f3n 1.1 Prop\u00f3sito El documento tiene como objetivo definir la estructura del sistema, es decir , establecer c\u00f3mo est\u00e1n organizados los componentes del software, c\u00f3mo interact\u00faan entre s\u00ed, y c\u00f3mo se integrar\u00e1n para formar un sistema cohesivo. 1.2 Alcance En el documento se especifica que habr\u00e1 diferentes diagramas los cuales podr\u00e1n ayudar a entender la arquitectura del sistema, adem\u00e1s de que estos diagramas cumpliran con los requerimientos funcionales, y no funcionales lo que ayudar\u00e1 a complementar el documento de requerimientos de software 1.3 Definiciones, Acr\u00f3nimos y Abreviaturas UML: El lenguaje unificado de modelado (UML, por sus siglas en ingl\u00e9s, Unified Modeling Language) es el lenguaje de modelado de sistemas de software m\u00e1s conocido y utilizado en la actualidad. API: es una pieza de c\u00f3digo que permite a dos aplicaciones comunicarse entre s\u00ed para compartir informaci\u00f3n y funcionalidades. Se usan generalmente en bibliotecas de programaci\u00f3n. 2. Representaci\u00f3n Arquitect\u00f3nica La arquitectura que mejor representa al sistema ser\u00eda la de microservicio, de las cual se puede obtener escalabilidad,resiliencia,flexibilidad tecnol\u00f3gica,facilidad de Mantenimiento. Este tipo de arquitectura permite tener servicios peque\u00f1os e independientes que se comunican entre s\u00ed a trav\u00e9s de APIs. Cada microservicio es responsable de una funcionalidad espec\u00edfica del sistema y puede ser desarrollado, desplegado, y escalado de manera independiente.. 2.1 Vista de Casos de Uso La vista de casos de uso es una representaci\u00f3n de los requisitos funcionales de un sistema, enfocada en c\u00f3mo los diferentes actores (usuarios o sistemas externos) interact\u00faan con el sistema para lograr sus objetivos. Esta vista se utiliza para capturar y describir las funcionalidades que el sistema debe ofrecer , desde la perspectiva de los usuarios y otras entidades externas que interact\u00faan con \u00e9l. 2.2 Vista L\u00f3gica: La vista l\u00f3gica es una de las principales perspectivas en la arquitectura de software que se enfoca en la organizaci\u00f3n y estructura interna del sistema desde el punto de vista del dise\u00f1o l\u00f3gico. Esta vista descompone el sistema en componentes o m\u00f3dulos, describiendo c\u00f3mo est\u00e1n organizados y c\u00f3mo interact\u00faan entre s\u00ed para cumplir con los requisitos funcionales. 2.3 Vista de Despliegue: La vista de despliegue es una de las perspectivas clave en la arquitectura de software que se enfoca en c\u00f3mo los componentes del sistema se distribuyen e instalan en el entorno f\u00edsico o virtual en el que operan. 2.4 Vista de Datos: La vista de datos en la arquitectura de software se centra en la organizaci\u00f3n, estructura, almacenamiento, y acceso a los datos dentro de un sistema. Esta vista es crucial para entender c\u00f3mo se manejan los datos a lo largo de todo el ciclo de vida de una aplicaci\u00f3n, desde su creaci\u00f3n y almacenamiento hasta su recuperaci\u00f3n y eliminaci\u00f3n. 3. Objetivos Arquitect\u00f3nicos y Restricciones 3.1 Objetivos Optimizar la velocidad con la que interact\u00faan los componentes. Facilitar la correcci\u00f3n de errores. Capacidad de cambiar componentes sin problemas. implementar autenticaci\u00f3n y autorizaci\u00f3n mediante tokens. 3.2 Restricciones No sobrecargar la aplicaci\u00f3n No dejar datos privados expuestos. 4. Vista de casos de uso 5. Vista de Componentes 6. Vista Despliegue 7. Tama\u00f1o y desempe\u00f1o Se espera que la aplicaci\u00f3n pueda albergar a alumnos de ingenier\u00eda en computaci\u00f3n, por lo que los usuarios conectados al mismo tiempo que podr\u00eda aguantar ser\u00eda alrededor de 200. La idea es que la respuesta del sistema sea r\u00e1pida, m\u00e1s que nada en la parte del chatbot, donde se espera que pueda calificar el ensayo en menos de 2 minutos. 8. Calidad Seguridad de autentificaci\u00f3n: autenticaci\u00f3n: Es necesario que los usuarios se identifiquen antes de usar la aplicaci\u00f3n para asegurarse que s\u00f3lo. Seguridad de datos: Mantener los ensayos enviados de manera segura con diferentes candados de seguridad para que no sean de f\u00e1cil acceso. Mantenibilidad: El sistema debe ser f\u00e1cil de mantener ."
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

