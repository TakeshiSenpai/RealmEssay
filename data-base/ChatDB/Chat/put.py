import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
chat_collection = db["Chat"]

# Función para actualizar un chat por su ID usando datos desde un archivo JSON
def actualizar_chat_desde_json(chat_id, archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            nuevos_datos = json.load(file)

        # Crear el diccionario de actualización
        actualizacion = {}
        if 'RespuestasIA' in nuevos_datos:
            actualizacion['RespuestasIA'] = nuevos_datos['RespuestasIA']
        if 'RespuestasAlumno' in nuevos_datos:
            actualizacion['RespuestasAlumno'] = nuevos_datos['RespuestasAlumno']
        
        # Actualizar el chat en la colección
        resultado = chat_collection.update_one(
            {"_id": ObjectId(chat_id)}, 
            {"$set": actualizacion}
        )

        if resultado.matched_count > 0:
            print(f"Chat con ID {chat_id} actualizado.")
        else:
            print(f"Chat con ID {chat_id} no encontrado.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
actualizar_chat_desde_json("671b3efee259173f17114f35", 'data.json')
