import json,pathlib
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
chat_collection = db["Chat"]

# Función para crear chats desde un archivo JSON
def crear_chat_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            chats = json.load(file)

        # Insertar los chats en la colección
        if isinstance(chats, list):
            resultado = chat_collection.insert_many(chats)
            print(f"{len(resultado.inserted_ids)} chats creados.")
        else:
            resultado = chat_collection.insert_one(chats)
            print(f"Chat creado con ID: {resultado.inserted_id}")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
test_path=pathlib.Path('database/ChatDB/Chat/chat_tests_files/data.json').resolve()
print(test_path)
crear_chat_desde_json(test_path)
