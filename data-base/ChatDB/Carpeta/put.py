import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Leer variables de entorno
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_cluster = os.getenv("MONGO_CLUSTER")

# Conexión a MongoDB
client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
carpeta_collection = db["Carpeta"]

# Función para actualizar una carpeta por su ID usando datos desde un archivo JSON que contiene objetos
def actualizar_carpeta_desde_json(carpeta_id, archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            nuevos_datos = json.load(file)

        # Si el campo "Chats" es una lista de objetos, conviértelo adecuadamente
        if isinstance(nuevos_datos.get("Chats"), list):
            for chat in nuevos_datos["Chats"]:
                if "ChatId" in chat:
                    chat["ChatId"] = ObjectId(chat["ChatId"])  # Convertir ChatId a ObjectId si es necesario
        
        # Actualizar la carpeta en la colección
        resultado = carpeta_collection.update_one(
            {"_id": ObjectId(carpeta_id)}, 
            {"$set": nuevos_datos}
        )

        if resultado.matched_count > 0:
            print(f"Carpeta con ID {carpeta_id} actualizada.")
        else:
            print(f"Carpeta con ID {carpeta_id} no encontrada.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
# Ejemplo de uso
actualizar_carpeta_desde_json("605c9a1b8cfa0d1c4cb7dbae", 'data.json')
