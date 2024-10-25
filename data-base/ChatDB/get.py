from pymongo import MongoClient
from pprint import pprint  # Importar pprint para mejor formato de impresión

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
chat_collection = db["chat"]  # Conexión a la colección "chat"

# Leer todos los prompts (chat)
def leer_prompts():
    prompts = chat_collection.find()
    for prompt in prompts:
        prompt['_id'] = str(prompt['_id'])  # Convertir ObjectId a string
        print("\n--- Prompt ---")
        pprint(prompt)

# Leer un prompt por su contenido
def leer_prompt_por_contenido(contenido):
    prompt = chat_collection.find_one({"Prompt": contenido})
    if prompt:
        prompt['_id'] = str(prompt['_id'])  # Convertir ObjectId a string
        print("\n--- Prompt encontrado ---")
        pprint(prompt)
    else:
        print(f"Prompt con el contenido '{contenido}' no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    print("\nPrompts actuales en la base de datos:")
    leer_prompts()

    print("\nBuscar prompt por contenido:")
    leer_prompt_por_contenido("¿Por qué mi calificación fue 85?")
