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
db = client["TareasDB"]
tarea_collection = db["Tarea"]

# Función para actualizar una tarea por su ID usando datos desde un archivo JSON
def actualizar_tarea_desde_json(tarea_id, archivo_json):
    try:
        # Leer el archivo JSON con codificación UTF-8
        with open(archivo_json, 'r', encoding='utf-8') as file:
            nuevos_datos = json.load(file)

        # Actualizar la tarea en la colección
        resultado = tarea_collection.update_one(
            {"_id": ObjectId(tarea_id)}, 
            {"$set": nuevos_datos}
        )

        if resultado.matched_count > 0:
            print(f"Tarea con ID {tarea_id} actualizada.")
        else:
            print(f"Tarea con ID {tarea_id} no encontrada.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e).encode('utf-8').decode('utf-8')}")

# Ejemplo de uso
if __name__ == "__main__":
    actualizar_tarea_desde_json("6739c4e5ea37f175c3833ed8", 'data.json')
