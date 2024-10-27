from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
carpeta_collection = db["Carpeta"]

# Función para actualizar una carpeta por su ID usando datos desde un archivo JSON
def actualizar_carpeta_desde_json(carpeta_id, archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            nuevos_datos = json.load(file)

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
actualizar_carpeta_desde_json("605c9a1b8cfa0d1c4cb7dbae", 'C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\RealmEssay\\data-base\\TareasDB\\Carpeta\\data.json')