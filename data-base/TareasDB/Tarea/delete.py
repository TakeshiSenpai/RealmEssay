from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
eliminar_tarea("605c9a1b8cfa0d1c4cb7dbae")
