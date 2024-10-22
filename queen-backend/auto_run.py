from multiprocessing import Process
import os

def api_gateway():
    os.system("python3 queen-backend/api_gateway.py")

def authentication():
    os.system("python3 queen-backend/server_authentication/google_auth.py")

def homework_teacher():
    os.system("python3 queen-backend/server_homework_teacher/homework_teacher.py")

def ia():
    os.system("python3 queen-backend/server_ia/ia.py")

if __name__ == "__main__":
    # Crear procesos para ejecutar los servidores
    p1 = Process(target= api_gateway)
    p2 = Process(target=authentication)
    p3 = Process(target=homework_teacher)
    p4 = Process(target=ia)

    # Iniciar ambos procesos
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Esperar a que ambos procesos terminen
    p1.join()
    p2.join()
    p3.join()
    p4.join()
