from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
exportar_carpetas_a_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\RealmEssay\\data-base\\ChatDB\\Carpeta\\data1.json')
