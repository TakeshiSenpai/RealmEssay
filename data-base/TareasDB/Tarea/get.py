import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
