import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Leer variables de entorno
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_cluster = os.getenv("MONGO_CLUSTER")

# Conexión a MongoDB
client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
alumno_collection = db["Alumno"]

# Función para exportar todos los alumnos a un archivo JSON
def exportar_alumnos_a_json(archivo_json):
    try:
        # Obtener todos los alumnos
        alumnos = list(alumno_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for alumno in alumnos:
            alumno['_id'] = str(alumno['_id'])
        
        # Escribir los alumnos en el archivo JSON con UTF-8
        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(alumnos, file, ensure_ascii=False, indent=4)
        
        print(f"Alumnos exportados a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {str(e).encode('utf-8').decode('utf-8')}")

# Función para buscar un alumno por ID
def buscar_alumno_por_id(alumno_id):
    try:
        # Buscar el alumno por su ID
        alumno = alumno_collection.find_one({"_id": ObjectId(alumno_id)})

        if alumno:
            # Convertir ObjectId a string para la salida JSON
            alumno['_id'] = str(alumno['_id'])

            # Imprimir el alumno encontrado en formato JSON legible
            print("Alumno encontrado:")
            print(json.dumps(alumno, ensure_ascii=False, indent=4))
            return alumno
        else:
            print(f"No se encontró ningún alumno con el ID: {alumno_id}")
            return None

    except Exception as e:
        print(f"Ocurrió un error al buscar el alumno por ID: {str(e).encode('utf-8').decode('utf-8')}")

# Ejemplo de uso
if __name__ == "__main__":
    # Exportar todos los datos a un archivo JSON (opcional)
    exportar_alumnos_a_json('data.json')

    # Buscar un alumno por ID
    alumno_id = "6739483de4679a6e126f0f13"  # Cambia esto por un ID válido de tu colección
    buscar_alumno_por_id(alumno_id)
