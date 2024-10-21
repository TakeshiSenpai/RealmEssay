import json
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
usuarios_collection = db["users"]

# Función para crear usuarios a partir de un archivo JSON
def crear_usuarios_desde_json(archivo_json):
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r') as file:
            datos = json.load(file)

        # Insertar los datos en la colección
        if isinstance(datos, list):
            resultado = usuarios_collection.insert_many(datos)
            print(f"{len(resultado.inserted_ids)} usuarios creados exitosamente.")
        elif isinstance(datos, dict):
            resultado = usuarios_collection.insert_one(datos)
            print(f"Usuario creado con ID: {resultado.inserted_id}")
        else:
            print("El formato del archivo JSON no es válido.")
    
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo_json}.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Path de el archivo JSON que se quiere enviar
    crear_usuarios_desde_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\data-base\\users\\data.json')
