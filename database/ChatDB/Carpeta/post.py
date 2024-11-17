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

# Función para crear una nueva carpeta desde un archivo JSON que contiene objetos
def crear_carpeta_desde_json(nombre_archivo_json):
    try:
        # Obtener la ruta del archivo JSON relativa a donde se ejecuta el script
        ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo_json)

        # Leer el archivo JSON
        with open(ruta_archivo, 'r') as file:
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
        print(f"Archivo {nombre_archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {nombre_archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
crear_carpeta_desde_json('data.json')
