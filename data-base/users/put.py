from pymongo import MongoClient
import re

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
usuarios_collection = db["users"]

# Mostrar todos los nombres en la base de datos
def listar_nombres():
    usuarios = usuarios_collection.find({}, {"Nombre": 1, "_id": 0})  # Solo obtener el campo "Nombre"
    print("Nombres en la base de datos:")
    for usuario in usuarios:
        print(usuario["Nombre"])

# Ejemplo de uso
if __name__ == "__main__":
    listar_nombres()

# Buscar usuario por nombre
def buscar_usuario_por_nombre(nombre):
    nombre = nombre.strip()  # Eliminar espacios en blanco
    print(f"Buscando usuario con nombre exacto: '{nombre}'")  # Depuración
    usuario = usuarios_collection.find_one({"Nombre": nombre})  # Búsqueda exacta sin regex
    if usuario:
        print(f"Usuario encontrado: {usuario}")
        return usuario
    else:
        print("Usuario no encontrado para búsqueda.")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    buscar_usuario_por_nombre("Gokú Actualizado")

# Actualizar el documento para corregir un nombre
def corregir_usuario_por_nombre(nombre_incorrecto, nuevo_nombre):
    usuario = buscar_usuario_por_nombre(nombre_incorrecto)
    if usuario:
        resultado = usuarios_collection.update_one({"Nombre": usuario["Nombre"]}, {"$set": {"Nombre": nuevo_nombre}})
        if resultado.matched_count > 0:
            print(f"Usuario actualizado correctamente a: {nuevo_nombre}")
        else:
            print("Error al intentar actualizar el usuario.")
    else:
        print("No se encontró el usuario para actualizar.")

# Ejemplo de uso
if __name__ == "__main__":
    # Corregir un nombre de usuario
    corregir_usuario_por_nombre("Goku Ramirez", "Goku Son")