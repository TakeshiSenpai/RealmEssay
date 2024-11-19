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
chat_collection = db["Chat"]

# Función para actualizar un chat por su ID usando datos desde un archivo JSON
def actualizar_chat_desde_json(chat_id, archivo_json):
    try:
        # Leer el archivo JSON con codificación UTF-8
        with open(archivo_json, 'r', encoding='utf-8') as file:
            datos = json.load(file)

        # Buscar el documento correcto en el archivo JSON
        chat_a_actualizar = next((item for item in datos if item["_id"] == chat_id), None)
        if not chat_a_actualizar:
            print(f"No se encontró un documento con el ID {chat_id} en el archivo {archivo_json}.")
            return

        # Eliminar el campo _id del documento para evitar conflictos
        if "_id" in chat_a_actualizar:
            del chat_a_actualizar["_id"]

        # Actualizar el chat en la colección
        resultado = chat_collection.update_one(
            {"_id": ObjectId(chat_id)},
            {"$set": chat_a_actualizar}
        )

        if resultado.matched_count > 0:
            print(f"Chat con ID {chat_id} actualizado exitosamente.")
        else:
            print(f"Chat con ID {chat_id} no encontrado en la base de datos.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    actualizar_chat_desde_json("673993b946e26957157fbc4e", 'chats.json')
