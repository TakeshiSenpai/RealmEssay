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
carpeta_collection = db["Carpeta"]

# Función para exportar carpetas que contienen objetos a un archivo JSON
def exportar_carpetas_a_json(archivo_json):
    try:
        # Obtener todas las carpetas
        carpetas = list(carpeta_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for carpeta in carpetas:
            carpeta['_id'] = str(carpeta['_id'])
            if "Chats" in carpeta and isinstance(carpeta['Chats'], list):
                carpeta['Chats'] = [str(chat['ChatId']) for chat in carpeta['Chats']]

        # Escribir las carpetas en el archivo JSON con UTF-8 y caracteres especiales
        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(carpetas, file, ensure_ascii=False, indent=4)
        
        print(f"Carpetas exportadas a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para obtener una carpeta por ID
def obtener_carpeta_por_id(carpeta_id):
    try:
        # Buscar el documento por su ID
        carpeta = carpeta_collection.find_one({"_id": ObjectId(carpeta_id)})

        # Verificar si se encontró el documento
        if carpeta:
            # Convertir ObjectId a string para serialización
            carpeta['_id'] = str(carpeta['_id'])
            if "Chats" in carpeta and isinstance(carpeta['Chats'], list):
                carpeta['Chats'] = [str(chat['ChatId']) for chat in carpeta['Chats']]
            
            # Imprimir el documento encontrado
            print("Carpeta encontrada:")
            print(json.dumps(carpeta, ensure_ascii=False, indent=4))
            return carpeta
        else:
            print(f"No se encontró ninguna carpeta con el ID: {carpeta_id}")
            return None
    
    except Exception as e:
        print(f"Ocurrió un error al obtener la carpeta por ID: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Exportar todos los datos a un archivo JSON (opcional)
    exportar_carpetas_a_json('data1.json')

    # Obtener una carpeta específica por su ID
    carpeta_id = "67399c4515e172b3a77629c2"  # Cambia esto por un ID válido de tu colección
    obtener_carpeta_por_id(carpeta_id)
