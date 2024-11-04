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
db = client["ChatDB"]
chat_collection = db["Chat"]

# Función para eliminar un chat por su ID
def eliminar_chat(chat_id):
    try:
        resultado = chat_collection.delete_one({"_id": ObjectId(chat_id)})
        if resultado.deleted_count > 0:
            print(f"Chat con ID {chat_id} eliminado.")
        else:
            print(f"Chat con ID {chat_id} no encontrado.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
eliminar_chat("671b3efee259173f17114f35")
