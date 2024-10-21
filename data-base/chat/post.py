import json
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
chat_collection = db["chat"]  # Conexión a la colección "chat"

# Función para crear un nuevo chat a partir de un archivo JSON
def crear_chat_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos = json.load(file)

        # Insertar los datos en la colección "chat"
        resultado = chat_collection.insert_one(datos)
        print(f"Prompt creado con ID: {resultado.inserted_id}")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    crear_chat_desde_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\data-base\\chat\\data.json')  # Llamada a la función con el archivo JSON
