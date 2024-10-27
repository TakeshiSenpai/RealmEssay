from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
eliminar_alumno("605c9a1b8cfa0d1c4cb7dbae")
