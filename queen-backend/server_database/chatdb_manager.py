import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

class ChatDBManager:
    def __init__(self):
        """
        Inicializa la conexión a MongoDB y define la base de datos.
        """
        # Cargar variables de entorno
        load_dotenv()
        mongo_user = os.getenv("MONGO_USER")
        mongo_password = os.getenv("MONGO_PASSWORD")
        mongo_cluster = os.getenv("MONGO_CLUSTER")

        # Conexión a MongoDB
        self.client = MongoClient(
            f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority&appName=Cluster0"
        )
        self.db = self.client["ChatDB"]
        self.collection = None

    def set_collection(self, collection_name):
        """
        Cambia la colección activa.
        :param collection_name: Nombre de la colección (por ejemplo, "Chat" o "Carpeta").
        """
        self.collection = self.db[collection_name]
        print(f"Colección activa: {collection_name}")

    def create_from_json_object(self, json_object):
        """
        Crea un documento en la colección activa desde un objeto JSON.
        :param json_object: Objeto JSON (puede ser un dict o una lista de dicts).
        """
        try:
            # Verifica si el objeto es una lista de documentos o un solo documento
            if isinstance(json_object, list):
                result = self.collection.insert_many(json_object)
                print(f"{len(result.inserted_ids)} documentos creados.")
            elif isinstance(json_object, dict):
                result = self.collection.insert_one(json_object)
                print(f"Documento creado con ID: {result.inserted_id}")
            else:
                print("El objeto JSON proporcionado no es válido. Debe ser un dict o una lista de dicts.")
        except Exception as e:
            print(f"Error al crear documento(s): {e}")


    # CRUD GENÉRICO

    def create_from_json(self, json_file):
        """
        Crea un documento en la colección activa desde un archivo JSON.
        :param json_file: Ruta del archivo JSON.
        """
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            if isinstance(data, list):
                result = self.collection.insert_many(data)
                print(f"{len(result.inserted_ids)} documentos creados.")
            else:
                result = self.collection.insert_one(data)
                print(f"Documento creado con ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error al crear documento(s): {e}")

    def read_all(self):
        """
        Lee todos los documentos de la colección activa.
        """
        try:
            documents = list(self.collection.find())
            for doc in documents:
                doc['_id'] = str(doc['_id'])  # Convertir ObjectId a string
            print("Documentos obtenidos:")
            for doc in documents:
                print(doc)
            return documents
        except Exception as e:
            print(f"Error al leer documentos: {e}")

    def read_by_id(self, document_id):
        """
        Lee un documento por su ID en la colección activa.
        :param document_id: ID del documento.
        """
        try:
            document = self.collection.find_one({"_id": ObjectId(document_id)})
            if document:
                document['_id'] = str(document['_id'])
                print("Documento encontrado:")
                print(document)
                return document
            else:
                print("Documento no encontrado")
        except Exception as e:
            print(f"Error al leer documento por ID: {e}")

    def update_by_id(self, document_id, json_file):
        """
        Actualiza un documento por su ID en la colección activa desde un archivo JSON.
        :param document_id: ID del documento.
        :param json_file: Ruta del archivo JSON con los datos para actualizar.
        """
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            result = self.collection.update_one(
                {"_id": ObjectId(document_id)},
                {"$set": data}
            )
            if result.matched_count > 0:
                print(f"Documento con ID {document_id} actualizado.")
            else:
                print("Documento no encontrado.")
        except Exception as e:
            print(f"Error al actualizar documento: {e}")

    def delete_by_id(self, document_id):
        """
        Elimina un documento por su ID en la colección activa.
        :param document_id: ID del documento.
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(document_id)})
            if result.deleted_count > 0:
                print(f"Documento con ID {document_id} eliminado.")
            else:
                print("Documento no encontrado.")
        except Exception as e:
            print(f"Error al eliminar documento: {e}")

    # MÉTODOS ESPECÍFICOS

    def buscar_carpeta_por_nombre(self, nombre_carpeta):
        """
        Busca carpetas por nombre (case insensitive).
        :param nombre_carpeta: Nombre de la carpeta.
        """
        try:
            resultados = list(self.collection.find({"Nombre": {"$regex": nombre_carpeta, "$options": "i"}}))
            for carpeta in resultados:
                carpeta['_id'] = str(carpeta['_id'])
            print(f"Carpetas encontradas con el nombre '{nombre_carpeta}':")
            for carpeta in resultados:
                print(carpeta)
            return resultados
        except Exception as e:
            print(f"Error al buscar carpetas: {e}")

    def buscar_chats_por_correo(self, correo_alumno):
        """
        Busca chats asociados a un correo de alumno.
        :param correo_alumno: Correo del alumno.
        """
        try:
            resultados = list(self.collection.find({"CorreoAlumno": correo_alumno}))
            for chat in resultados:
                chat['_id'] = str(chat['_id'])
            print(f"Chats encontrados para el correo '{correo_alumno}':")
            for chat in resultados:
                print(chat)
            return resultados
        except Exception as e:
            print(f"Error al buscar chats: {e}")
