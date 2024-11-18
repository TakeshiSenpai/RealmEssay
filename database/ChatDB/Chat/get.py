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

# Función para exportar todos los chats a un archivo JSON
def exportar_chats_a_json(archivo_json):
    try:
        # Obtener todos los chats
        chats = list(chat_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for chat in chats:
            chat['_id'] = str(chat['_id'])

        # Escribir los chats en el archivo JSON con UTF-8
        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(chats, file, ensure_ascii=False, indent=4)
        
        print(f"Chats exportados a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para obtener un chat por ID
def obtener_chat_por_id(chat_id):
    try:
        # Buscar el documento por su ID
        chat = chat_collection.find_one({"_id": ObjectId(chat_id)})

        # Verificar si se encontró el documento
        if chat:
            # Convertir ObjectId a string para serialización
            chat['_id'] = str(chat['_id'])
            
            # Imprimir el documento encontrado
            print("Chat encontrado:")
            print(json.dumps(chat, ensure_ascii=False, indent=4))
            return chat
        else:
            print(f"No se encontró ningún chat con el ID: {chat_id}")
            return None
    
    except Exception as e:
        print(f"Ocurrió un error al obtener el chat por ID: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Exportar todos los datos a un archivo JSON (opcional)
    exportar_chats_a_json('chats.json')

    # Obtener un chat específico por su ID
    chat_id = "673993b946e26957157fbc4e"  # Cambia esto por un ID válido de tu colección
    obtener_chat_por_id(chat_id)
