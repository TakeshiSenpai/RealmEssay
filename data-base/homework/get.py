from pymongo import MongoClient
from pprint import pprint  # Importar pprint para mejor formato de impresión

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
homeworks_collection = db["homeworks"]

# Leer todos los ensayos (homeworks)
def leer_ensayos():
    ensayos = homeworks_collection.find()
    for ensayo in ensayos:
        ensayo['_id'] = str(ensayo['_id'])  # Convertir ObjectId a string
        print("\n--- Ensayo ---")
        pprint(ensayo)

# Leer un ensayo por título
def leer_ensayo_por_titulo(titulo):
    ensayo = homeworks_collection.find_one({"Ensayo": titulo})
    if ensayo:
        ensayo['_id'] = str(ensayo['_id'])  # Convertir ObjectId a string
        print("\n--- Ensayo encontrado ---")
        pprint(ensayo)
    else:
        print(f"Ensayo con título '{titulo}' no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    print("\nEnsayos actuales en la base de datos:")
    leer_ensayos()

    print("\nBuscar ensayo por título:")
    leer_ensayo_por_titulo("Inteligencia Artificial")
