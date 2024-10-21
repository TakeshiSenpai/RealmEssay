from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
homeworks_collection = db["homeworks"]

# Mostrar todos los títulos de ensayos en la base de datos
def listar_titulos():
    ensayos = homeworks_collection.find({}, {"Ensayo": 1, "_id": 0})  # Solo obtener el campo "Ensayo"
    print("Ensayos en la base de datos:")
    for ensayo in ensayos:
        print(ensayo["Ensayo"])

# Buscar ensayo por título
def buscar_ensayo_por_titulo(titulo):
    titulo = titulo.strip()  # Eliminar espacios en blanco
    print(f"Buscando ensayo con título exacto: '{titulo}'")  # Depuración
    ensayo = homeworks_collection.find_one({"Ensayo": titulo})  # Búsqueda exacta sin regex
    if ensayo:
        print(f"Ensayo encontrado: {ensayo}")
        return ensayo
    else:
        print("Ensayo no encontrado para búsqueda.")
        return None

# Eliminar un ensayo por título
def eliminar_ensayo_por_titulo(titulo):
    ensayo = buscar_ensayo_por_titulo(titulo)
    if ensayo:
        resultado = homeworks_collection.delete_one({"Ensayo": ensayo["Ensayo"]})
        if resultado.deleted_count > 0:
            print(f"Ensayo '{titulo}' eliminado correctamente.")
        else:
            print(f"Error al intentar eliminar el ensayo '{titulo}'.")
    else:
        print(f"No se encontró el ensayo '{titulo}' para eliminar.")

# Ejemplo de uso
if __name__ == "__main__":
    # Listar los ensayos
    listar_titulos()

    # Eliminar un ensayo
    eliminar_ensayo_por_titulo("Inteligencia Artificial")
