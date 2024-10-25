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

# Actualizar un campo en el prompt basado en su contenido
def corregir_prompt_por_contenido(prompt_incorrecto, nuevos_datos):
    prompt = buscar_prompt_por_contenido(prompt_incorrecto)
    if prompt:
        resultado = chat_collection.update_one({"Prompt": prompt["Prompt"]}, {"$set": nuevos_datos})
        if resultado.matched_count > 0:
            print(f"Prompt '{prompt_incorrecto}' actualizado correctamente con los siguientes datos: {nuevos_datos}")
        else:
            print("Error al intentar actualizar el prompt.")
    else:
        print("No se encontró el prompt para actualizar.")

# Ejemplo de uso
if __name__ == "__main__":
    # Listar todos los prompts
    listar_prompts()

    # Actualizar el campo "Fecha y Hora" de un prompt específico
    nuevos_datos = {"Fecha y Hora": "2024-10-20 16:00:00"}
    corregir_prompt_por_contenido("Â¿Por que mi calificacion fue 85", nuevos_datos)
