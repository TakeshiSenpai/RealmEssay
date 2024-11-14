import os
from multiprocessing import Process

def run_python_file(file_path):
    if not os.path.exists(file_path):
        file_path = f"queen-backend/{file_path}"
    os.system(f"python3 {file_path}")

def api_gateway():
    run_python_file("api_gateway.py")

def authentication():
    run_python_file("server_authentication/google_auth.py")

def homework_teacher():
    run_python_file("server_homework_teacher/homework_teacher.py")

def ia():
    run_python_file("server_ia/ia.py")

def homework_student():
    run_python_file("server_homework_student/homework_student.py")

# def db():
    #run_python_file("database/maindb.py")

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