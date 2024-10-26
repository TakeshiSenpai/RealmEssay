import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
carpeta_collection = db["Carpeta"]

# Función para eliminar una carpeta por su ID
def eliminar_carpeta(carpeta_id):
    try:
        resultado = carpeta_collection.delete_one({"_id": ObjectId(carpeta_id)})
        if resultado.deleted_count > 0:
            print(f"Carpeta con ID {carpeta_id} eliminada.")
        else:
            print(f"Carpeta con ID {carpeta_id} no encontrada.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
eliminar_carpeta("671b464bcf72d845cf4c6616")
