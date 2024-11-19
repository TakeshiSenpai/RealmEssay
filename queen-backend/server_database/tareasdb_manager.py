import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

class TareasDBManager:
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
        self.db = self.client["TareasDB"]
        self.collection = None

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


    def set_collection(self, collection_name):
        """
        Cambia la colección activa.
        :param collection_name: Nombre de la colección (por ejemplo, "Alumno" o "Tarea").
        """
        self.collection = self.db[collection_name]
        print(f"Colección activa: {collection_name}")

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

    # MÉTODOS ESPECÍFICOS PARA ALUMNO Y TAREA

    def buscar_alumnos_por_calificacion(self, calificacion_minima):
        """
        Busca alumnos con calificaciones mayores o iguales a una calificación mínima.
        :param calificacion_minima: Calificación mínima.
        """
        try:
            resultados = list(self.collection.find({"Calificacion": {"$gte": calificacion_minima}}))
            for alumno in resultados:
                alumno['_id'] = str(alumno['_id'])
            print(f"Alumnos con calificación >= {calificacion_minima}:")
            for alumno in resultados:
                print(alumno)
            return resultados
        except Exception as e:
            print(f"Error al buscar alumnos: {e}")
