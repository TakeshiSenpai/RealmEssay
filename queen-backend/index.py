import os, pathlib
from multiprocessing import Process
from pydoc import resolve

def run_python_file(file_path):
    #entorno_virtiual = pathlib.Path(".venv/Scripts/Python.exe").resolve()
    entorno_virtiual = "python"
    print(entorno_virtiual) #Print de debug para mirar la ruta, borrenlo cuando todos puedan correrlo
    if not os.path.exists(file_path):
        file_path = f"queen-backend/{file_path}"
    os.system(f"{entorno_virtiual} {file_path}")
    #Cambio para que funcionara con el entorno virtual
    #Si no quieren el entorno virtual cambien la variable entorno_virtiual = "python" ó entorno_virtiual ="python3"
    #En Mac es pathlib.Path(".venv/bin/Python").resolve()
def api_gateway():
    run_python_file("api_gateway/api_gateway.py")

def authentication():
    run_python_file("server_authentication/api/index.py")

def homework_teacher():
    run_python_file("server_homework_teacher/api/index.py")

def ia():
    run_python_file("server_ia/api/index.py")
# def db):
    #run_python_file("database/maindb.py")

def homework_student():
    run_python_file("server_homework_student/api/index.py")

if __name__ == "__main__":

    # Crear procesos para ejecutar los servidores
    p1 = Process(target=api_gateway)
    p2 = Process(target=authentication)
    p3 = Process(target=homework_teacher)
    p4 = Process(target=ia)
    p5 = Process(target=homework_student)

    # Iniciar los procesos
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()