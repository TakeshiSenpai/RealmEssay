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

# Función para actualizar una carpeta por su ID usando datos desde un archivo JSON
def actualizar_carpeta_desde_json(carpeta_id, archivo_json):
    try:
        # Leer el archivo JSON con codificación UTF-8
        with open(archivo_json, 'r', encoding='utf-8') as file:
            datos = json.load(file)

        # Buscar el documento correcto en el archivo JSON
        carpeta_a_actualizar = next((item for item in datos if item["_id"] == carpeta_id), None)
        if not carpeta_a_actualizar:
            print(f"No se encontró un documento con el ID {carpeta_id} en el archivo {archivo_json}.")
            return

        # Eliminar el campo _id del documento para evitar el error
        if "_id" in carpeta_a_actualizar:
            del carpeta_a_actualizar["_id"]

        # Convertir los ObjectIds en el JSON a tipo ObjectId si es necesario
        if "Chats" in carpeta_a_actualizar and isinstance(carpeta_a_actualizar["Chats"], list):
            carpeta_a_actualizar["Chats"] = [
                ObjectId(chat) if isinstance(chat, str) else chat for chat in carpeta_a_actualizar["Chats"]
            ]
        
        if "Carpeta" in carpeta_a_actualizar and "Chats" in carpeta_a_actualizar["Carpeta"]:
            for chat in carpeta_a_actualizar["Carpeta"]["Chats"]:
                if "ChatId" in chat:
                    chat["ChatId"] = ObjectId(chat["ChatId"])

        # Actualizar el documento en MongoDB
        resultado = carpeta_collection.update_one(
            {"_id": ObjectId(carpeta_id)},
            {"$set": carpeta_a_actualizar}
        )

        if resultado.matched_count > 0:
            print(f"Carpeta con ID {carpeta_id} actualizada exitosamente.")
        else:
            print(f"Carpeta con ID {carpeta_id} no encontrada en la base de datos.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    actualizar_carpeta_desde_json("673977bf9ec890adf2fef69a", 'data1.json')
