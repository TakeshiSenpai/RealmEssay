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

# Función para eliminar un alumno por su ID
def eliminar_alumno(alumno_id):
    try:
        resultado = alumno_collection.delete_one({"_id": ObjectId(alumno_id)})
        if resultado.deleted_count > 0:
            print(f"Alumno con ID {alumno_id} eliminado.")
        else:
            print(f"Alumno con ID {alumno_id} no encontrado.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
eliminar_alumno("6739483de4679a6e126f0f13")
