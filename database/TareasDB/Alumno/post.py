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

# Función para crear alumnos desde un archivo JSON
def crear_alumno_desde_json(archivo_json):
    try:
        # Leer el archivo JSON con codificación UTF-8
        with open(archivo_json, 'r', encoding='utf-8') as file:
            datos_alumno = json.load(file)

        # Insertar los datos en la colección
        if isinstance(datos_alumno, list):
            resultado = alumno_collection.insert_many(datos_alumno)
            print(f"{len(resultado.inserted_ids)} alumnos creados.")
        elif isinstance(datos_alumno, dict):
            resultado = alumno_collection.insert_one(datos_alumno)
            print(f"Alumno creado con ID: {resultado.inserted_id}")
        else:
            print("El archivo JSON no contiene un formato válido (debe ser un objeto o una lista de objetos).")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e).encode('utf-8').decode('utf-8')}")

# Ejemplo de uso
if __name__ == "__main__":
    crear_alumno_desde_json('data.json')
