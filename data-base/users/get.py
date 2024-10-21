from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
usuarios_collection = db["users"]

# Leer todos los usuarios
def leer_usuarios():
    usuarios = usuarios_collection.find()
    for usuario in usuarios:
        print(usuario)

# Leer un usuario por correo
def leer_usuario_por_correo(correo):
    usuario = usuarios_collection.find_one({"Correo": correo})
    if usuario:
        print(usuario)
    else:
        print("Usuario no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    print("\nUsuarios actuales en la base de datos:")
    leer_usuarios()

    print("\nBuscar usuario por correo:")
    leer_usuario_por_correo("goku.ram@uabc.edu.mx")
