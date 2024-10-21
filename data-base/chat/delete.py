from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatbotDB"]
chat_collection = db["chat"]  # Conexión a la colección "chat"

# Mostrar todos los prompts en la base de datos
def listar_prompts():
    prompts = chat_collection.find({}, {"Prompt": 1, "_id": 0})  # Solo obtener el campo "Prompt"
    print("Prompts en la base de datos:")
    for prompt in prompts:
        print(prompt["Prompt"])

# Buscar un prompt por su contenido
def buscar_prompt_por_contenido(prompt_text):
    prompt_text = prompt_text.strip()  # Eliminar espacios en blanco
    print(f"Buscando prompt con contenido exacto: '{prompt_text}'")  # Depuración
    prompt = chat_collection.find_one({"Prompt": prompt_text})  # Búsqueda exacta sin regex
    if prompt:
        print(f"Prompt encontrado: {prompt}")
        return prompt
    else:
        print("Prompt no encontrado para búsqueda.")
        return None

# Eliminar un prompt por su contenido
def eliminar_prompt_por_contenido(prompt_text):
    prompt = buscar_prompt_por_contenido(prompt_text)
    if prompt:
        resultado = chat_collection.delete_one({"Prompt": prompt["Prompt"]})
        if resultado.deleted_count > 0:
            print(f"Prompt '{prompt_text}' eliminado correctamente.")
        else:
            print(f"Error al intentar eliminar el prompt '{prompt_text}'.")
    else:
        print(f"No se encontró el prompt '{prompt_text}' para eliminar.")

# Ejemplo de uso
if __name__ == "__main__":
    # Listar todos los prompts
    listar_prompts()

    # Eliminar un prompt por su contenido
    eliminar_prompt_por_contenido("¿Por que mi calificación fue 85?")
