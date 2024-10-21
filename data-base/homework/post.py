import json
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
homeworks_collection = db["homeworks"]  # Conexión a la colección "homeworks"

# Función para crear un nuevo trabajo (homework) a partir de un archivo JSON
def crear_homework_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos = json.load(file)

        # Insertar los datos en la colección "homeworks"
        resultado = homeworks_collection.insert_one(datos)
        print(f"Ensayo creado con ID: {resultado.inserted_id}")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    crear_homework_desde_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\data-base\\homework\\ensayo.json')  # Llamada a la función con el archivo JSON
