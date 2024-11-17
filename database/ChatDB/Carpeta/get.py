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


# Función para exportar carpetas que contienen objetos a un archivo JSON
def exportar_carpetas_a_json(archivo_json):
    try:
        # Obtener todas las carpetas
        carpetas = list(carpeta_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for carpeta in carpetas:
            carpeta['_id'] = str(carpeta['_id'])
            carpeta['Chats'] = [str(chat['ChatId']) for chat in carpeta['Chats']]
        
        # Escribir las carpetas en el archivo JSON
        with open(archivo_json, 'w') as file:
            json.dump(carpetas, file, indent=4)
        
        print(f"Carpetas exportadas a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
exportar_carpetas_a_json('data1.json')
