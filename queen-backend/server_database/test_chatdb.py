from chatdb_manager import ChatDBManager

# Crear una instancia de ChatDBManager
chat_db = ChatDBManager()

# 1. Prueba para la colección 'Carpeta'
print("Prueba para la colección 'Carpeta'...\n")

# Cambiar a la colección 'Carpeta'
chat_db.set_collection("Carpeta")

# Crear documentos en la colección 'Carpeta' desde un archivo JSON
print("Creando documentos en la colección 'Carpeta'...")
chat_db.create_from_json("carpeta.json")

# Leer todos los documentos de la colección 'Carpeta'
print("\nLeyendo todos los documentos en la colección 'Carpeta'...")
carpetas = chat_db.read_all()

# Leer un documento específico por su ID
if carpetas:
    primer_id = carpetas[0]['_id']
    print(f"\nLeyendo documento con ID: {primer_id}...")
    chat_db.read_by_id(primer_id)

# Actualizar un documento por su ID
print("\nActualizando el primer documento...")
chat_db.update_by_id(primer_id, "actualizacion_carpeta.json")

# Eliminar un documento por su ID
print("\nEliminando el primer documento...")
chat_db.delete_by_id(primer_id)

# Buscar carpetas por nombre
print("\nBuscando carpetas con el nombre 'Matemáticas'...")
chat_db.buscar_carpeta_por_nombre("Matemáticas")

# 2. Prueba para la colección 'Chat'
print("\nPrueba para la colección 'Chat'...\n")

# Cambiar a la colección 'Chat'
chat_db.set_collection("Chat")

# Crear documentos en la colección 'Chat' desde un archivo JSON
print("Creando documentos en la colección 'Chat'...")
chat_db.create_from_json("chat.json")

# Leer todos los documentos de la colección 'Chat'
print("\nLeyendo todos los documentos en la colección 'Chat'...")
chats = chat_db.read_all()

# Leer un documento específico por su ID
if chats:
    primer_id_chat = chats[0]['_id']
    print(f"\nLeyendo documento con ID: {primer_id_chat}...")
    chat_db.read_by_id(primer_id_chat)

# Actualizar un documento por su ID
print("\nActualizando el primer documento de Chat...")
chat_db.update_by_id(primer_id_chat, "actualizacion_chat.json")

# Eliminar un documento por su ID
print("\nEliminando el primer documento de Chat...")
chat_db.delete_by_id(primer_id_chat)

# Buscar chats por correo
print("\nBuscando chats para el correo 'alumno1@example.com'...")
chat_db.buscar_chats_por_correo("alumno1@example.com")
