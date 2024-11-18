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

# Función para buscar una tarea por ID
def buscar_tarea_por_id(tarea_id, archivo_json=None):
    try:
        # Buscar la tarea por su ID
        tarea = tarea_collection.find_one({"_id": ObjectId(tarea_id)})

        if tarea:
            # Convertir ObjectId a string para que sea serializable en JSON
            tarea['_id'] = str(tarea['_id'])

            # Si se proporciona un archivo JSON, exportar los datos
            if archivo_json:
                with open(archivo_json, 'w', encoding='utf-8') as file:
                    json.dump(tarea, file, ensure_ascii=False, indent=4)
                print(f"Tarea exportada a {archivo_json}")

            # Imprimir la tarea en la consola en formato JSON
            print("Tarea encontrada:")
            print(json.dumps(tarea, ensure_ascii=False, indent=4))
            return tarea
        else:
            print(f"No se encontró ninguna tarea con el ID: {tarea_id}")
            return None

    except Exception as e:
        print(f"Ocurrió un error: {str(e).encode('utf-8').decode('utf-8')}")

# Ejemplo de uso
if __name__ == "__main__":
    # ID de la tarea a buscar (reemplazar por un ID válido en tu base de datos)
    tarea_id = "6739c4e5ea37f175c3833ed8"
    buscar_tarea_por_id(tarea_id, 'data1.json')
