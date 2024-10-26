import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
tarea_collection = db["Tarea"]

# Función para crear una nueva tarea desde un archivo JSON
def crear_tarea_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos_tarea = json.load(file)

        # Insertar la tarea en la colección
        resultado = tarea_collection.insert_one(datos_tarea)
        print(f"Tarea creada con ID: {resultado.inserted_id}")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
crear_tarea_desde_json('data.json')
