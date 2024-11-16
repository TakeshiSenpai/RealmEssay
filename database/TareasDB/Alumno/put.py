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

# Función para actualizar un alumno por su ID usando datos desde un archivo JSON
def actualizar_alumno_desde_json(alumno_id, archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            nuevos_datos = json.load(file)

        # Actualizar el alumno en la colección
        resultado = alumno_collection.update_one(
            {"_id": ObjectId(alumno_id)}, 
            {"$set": nuevos_datos}
        )

        if resultado.matched_count > 0:
            print(f"Alumno con ID {alumno_id} actualizado.")
        else:
            print(f"Alumno con ID {alumno_id} no encontrado.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
actualizar_alumno_desde_json("605c9a1b8cfa0d1c4cb7dbae", 'data.json')
