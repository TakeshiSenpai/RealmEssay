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

# Función para obtener todos los documentos de la colección 'Tarea'
def obtener_todas_las_tareas(archivo_json=None):
    try:
        # Obtener todas las tareas
        tareas = list(tarea_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for tarea in tareas:
            tarea['_id'] = str(tarea['_id'])

        # Si se proporciona un archivo JSON, exportar los datos
        if archivo_json:
            with open(archivo_json, 'w') as file:
                json.dump(tareas, file, indent=4)
            print(f"Datos exportados a {archivo_json}")

        # Imprimir tareas en la consola
        print("Datos obtenidos de la colección 'Tarea':")
        for tarea in tareas:
            print(tarea)
        
        return tareas

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Exportar todos los datos a un archivo JSON (opcional)
    obtener_todas_las_tareas('tareas.json')
