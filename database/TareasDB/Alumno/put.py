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
alumno_collection = db["Alumno"]

# Función para actualizar un alumno desde un archivo JSON con lista de objetos
def actualizar_alumno_desde_json(archivo_json):
    try:
        # Leer el archivo JSON con codificación UTF-8
        with open(archivo_json, 'r', encoding='utf-8') as file:
            datos_alumnos = json.load(file)

        # Verificar que sea una lista
        if isinstance(datos_alumnos, list):
            for alumno in datos_alumnos:
                if "_id" in alumno:
                    alumno["_id"] = ObjectId(alumno["_id"])  # Convertir _id a ObjectId

                # Extraer el ID y removerlo de los datos para la actualización
                alumno_id = alumno.pop("_id")
                resultado = alumno_collection.update_one(
                    {"_id": alumno_id},
                    {"$set": alumno}
                )

                if resultado.matched_count > 0:
                    print(f"Alumno con ID {alumno_id} actualizado.")
                else:
                    print(f"Alumno con ID {alumno_id} no encontrado.")
        else:
            print("El archivo JSON debe contener una lista de objetos.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e).encode('utf-8').decode('utf-8')}")

# Ejemplo de uso
if __name__ == "__main__":
    actualizar_alumno_desde_json('data.json')
