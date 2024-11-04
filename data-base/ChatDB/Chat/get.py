from flask import Flask, jsonify
import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Leer variables de entorno
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_cluster = os.getenv("MONGO_CLUSTER")

# Conexión a MongoDB
client = MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ChatDB"]
chat_collection = db["Chat"]

# Inicializar la aplicación Flask
app = Flask(__name__)

# Endpoint para obtener todos los chats
@app.route('/chats', methods=['GET'])
def obtener_chats():
    try:
        # Obtener todos los chats
        chats = list(chat_collection.find())

        # Convertir ObjectId a string para que sea serializable en JSON
        for chat in chats:
            chat['_id'] = str(chat['_id'])
        
        # Devolver los chats en formato JSON
        return jsonify(chats)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
