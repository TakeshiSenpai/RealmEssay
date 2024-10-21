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

# Ejemplo de uso
if __name__ == "__main__":
    listar_titulos()

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

# Ejemplo de uso
if __name__ == "__main__":
    buscar_ensayo_por_titulo("Inteligencia Artificial")

# Actualizar un campo en el ensayo basado en su título
def corregir_ensayo_por_titulo(titulo_incorrecto, nuevos_datos):
    ensayo = buscar_ensayo_por_titulo(titulo_incorrecto)
    if ensayo:
        resultado = homeworks_collection.update_one({"Ensayo": ensayo["Ensayo"]}, {"$set": nuevos_datos})
        if resultado.matched_count > 0:
            print(f"Ensayo '{titulo_incorrecto}' actualizado correctamente con los siguientes datos: {nuevos_datos}")
        else:
            print("Error al intentar actualizar el ensayo.")
    else:
        print("No se encontró el ensayo para actualizar.")

# Ejemplo de uso
if __name__ == "__main__":
    # Actualizar la rúbrica del ensayo con el título "Inteligencia Artificial"
    nuevos_datos = {"Rubrica": "Claridad, originalidad, y creatividad."}
    corregir_ensayo_por_titulo("Inteligencia Artificial", nuevos_datos)
