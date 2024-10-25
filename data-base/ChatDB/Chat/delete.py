import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
