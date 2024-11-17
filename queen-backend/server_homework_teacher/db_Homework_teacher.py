from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient(
    "mongodb+srv://alan11gt:ioUvPgAvDZcVwWXs@cluster0.2b8il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["TareasDB"]
tarea_collection = db["Tarea"]

#Este metodo es para hacer post a la base de datos de tareas del profesor
#Se le debe enviar el request que se obtiene de la conexion del frontend
def post(request):
    email = request.get("email")
    
    pass

