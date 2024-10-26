from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
alumno_collection = db["Alumno"]

# Función para obtener todos los alumnos y exportarlos a un archivo JSON
def exportar_alumnos_a_json(archivo_json):
    try:
        # Obtener todos los alumnos
        alumnos = list(alumno_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for alumno in alumnos:
            alumno['_id'] = str(alumno['_id'])
        
        # Escribir los alumnos en el archivo JSON
        with open(archivo_json, 'w') as file:
            json.dump(alumnos, file, indent=4)
        
        print(f"Alumnos exportados a {archivo_json}")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
exportar_alumnos_a_json('C:\\Users\\alan1\\Documents\\GitHub\\RealmEssay\\RealmEssay\\data-base\\TareasDB\\Alumno\\data.json')
