import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
alumno_collection = db["Alumno"]

# Función para crear un nuevo alumno desde un archivo JSON
def crear_alumno_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos_alumno = json.load(file)

        # Insertar el alumno en la colección
        resultado = alumno_collection.insert_one(datos_alumno)
        print(f"Alumno creado con ID: {resultado.inserted_id}")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
crear_alumno_desde_json('data.json')
