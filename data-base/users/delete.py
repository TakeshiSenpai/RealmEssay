from pymongo import MongoClient
import re

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
usuarios_collection = db["users"]

# Eliminar usuario por nombre usando expresión regular
def eliminar_usuario(nombre):
    resultado = usuarios_collection.delete_one({"Nombre": re.compile(f"^{nombre.strip()}$", re.IGNORECASE)})
    if resultado.deleted_count > 0:
        print(f"Usuario con nombre {nombre} eliminado correctamente.")
    else:
        print("Usuario no encontrado para eliminar.")

# Ejemplo de uso
if __name__ == "__main__":
    print("\nEliminando usuario:")
    eliminar_usuario("Gokú Son")
