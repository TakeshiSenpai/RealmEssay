import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
chat_collection = db["Chat"]
# Función para obtener todos los chats y exportarlos a un archivo JSON
def exportar_chats_a_json(archivo_json):
    try:
        # Obtener todos los chats
        chats = list(chat_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for chat in chats:
            chat['_id'] = str(chat['_id'])
        
        # Escribir los chats en el archivo JSON
        with open(archivo_json, 'w') as file:
            json.dump(chats, file, indent=4)
        
        print(f"Chats exportados a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
exportar_chats_a_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\RealmEssay\\data-base\\ChatDB\\Chat\\data1.json')
