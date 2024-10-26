import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
carpeta_collection = db["Carpeta"]

# Función para obtener todas las carpetas y exportarlas a un archivo JSON
def exportar_carpetas_a_json(archivo_json):
    try:
        # Obtener todas las carpetas
        carpetas = list(carpeta_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for carpeta in carpetas:
            carpeta['_id'] = str(carpeta['_id'])
        
        # Escribir las carpetas en el archivo JSON
        with open(archivo_json, 'w') as file:
            json.dump(carpetas, file, indent=4)
        
        print(f"Carpetas exportadas a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
exportar_carpetas_a_json('data.json')
