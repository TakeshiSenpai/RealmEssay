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

# Función para eliminar una tarea por su ID
def eliminar_tarea(tarea_id):
    try:
        resultado = tarea_collection.delete_one({"_id": ObjectId(tarea_id)})
        if resultado.deleted_count > 0:
            print(f"Tarea con ID {tarea_id} eliminada.")
        else:
            print(f"Tarea con ID {tarea_id} no encontrada.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
eliminar_tarea("6739c4e5ea37f175c3833ed8")
