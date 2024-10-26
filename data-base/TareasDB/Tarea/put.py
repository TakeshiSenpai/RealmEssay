import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
tarea_collection = db["Tarea"]

# Función para actualizar una tarea por su ID usando datos desde un archivo JSON
def actualizar_tarea_desde_json(tarea_id, archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            nuevos_datos = json.load(file)

        # Actualizar la tarea en la colección
        resultado = tarea_collection.update_one(
            {"_id": ObjectId(tarea_id)}, 
            {"$set": nuevos_datos}
        )

        if resultado.matched_count > 0:
            print(f"Tarea con ID {tarea_id} actualizada.")
        else:
            print(f"Tarea con ID {tarea_id} no encontrada.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
actualizar_tarea_desde_json("605c9a1b8cfa0d1c4cb7dbae", 'data.json')
