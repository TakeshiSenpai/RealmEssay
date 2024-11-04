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
tarea_collection = db["Tarea"]

# Función para obtener todas las tareas y exportarlas a un archivo JSON
def exportar_tareas_a_json(archivo_json):
    try:
        # Obtener todas las tareas
        tareas = list(tarea_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for tarea in tareas:
            tarea['_id'] = str(tarea['_id'])
        
        # Escribir las tareas en el archivo JSON
        with open(archivo_json, 'w') as file:
            json.dump(tareas, file, indent=4)
        
        print(f"Tareas exportadas a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
exportar_tareas_a_json('data.json')
