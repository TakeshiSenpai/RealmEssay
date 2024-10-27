from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
alumno_collection = db["Alumno"]

# Función para actualizar un alumno por su ID usando datos desde un archivo JSON
def actualizar_alumno_desde_json(alumno_id, archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            nuevos_datos = json.load(file)

        # Actualizar el alumno en la colección
        resultado = alumno_collection.update_one(
            {"_id": ObjectId(alumno_id)}, 
            {"$set": nuevos_datos}
        )

        if resultado.matched_count > 0:
            print(f"Alumno con ID {alumno_id} actualizado.")
        else:
            print(f"Alumno con ID {alumno_id} no encontrado.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
actualizar_alumno_desde_json("605c9a1b8cfa0d1c4cb7dbae", 'C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\RealmEssay\\data-base\\TareasDB\\Alumno\\data.json')