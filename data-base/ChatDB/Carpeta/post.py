import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
carpeta_collection = db["Carpeta"]

# Función para crear una nueva carpeta desde un archivo JSON que contiene objetos
def crear_carpeta_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos_carpeta = json.load(file)

        # Si el campo "Chats" es una lista de objetos, conviértelo adecuadamente
        if isinstance(datos_carpeta.get("Chats"), list):
            for chat in datos_carpeta["Chats"]:
                if "ChatId" in chat:
                    chat["ChatId"] = ObjectId(chat["ChatId"])  # Convertir ChatId a ObjectId si es necesario
        
        # Insertar la carpeta en la colección
        resultado = carpeta_collection.insert_one(datos_carpeta)
        print(f"Carpeta creada con ID: {resultado.inserted_id}")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
crear_carpeta_desde_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\RealmEssay\\data-base\\ChatDB\\Carpeta\\data.json')
