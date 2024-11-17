# Bases de datos
# ChatDB y TareasDB

Este proyecto implementa un sistema de gestión de tareas académicas utilizando MongoDB y Python. Incluye operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para cinco colecciones principales: En la base de datos **TareasDB:** **Alumno**, **Carpeta**, **Tarea** y en la base de datos **ChatDB:** **Chat**, **Carpeta**.

## Estructura del Proyecto

El proyecto consta de las siguientes colecciones en la base de datos `TareasDB`:

1. **Alumno**: Gestión de la información de los alumnos, como el correo electrónico, las entregas de tareas y la calificación.
2. **Carpeta**: Administración de carpetas que agrupan tareas y alumnos asociados.
3. **Tarea**: Gestión de las tareas, que incluye descripciones, rúbricas y alumnos asignados.

`ChatDB`:
1. **Carpeta**: Gestión de la información del profesor como lo son sus carpetas para organizarse, su correo electrónico, nombres de los alumnos y chats.
2. **Chat**: Manejo de la información de los chats de los alumnos, correo electrónico del alumno, prompts y respuestas de la IA.
## Requisitos

Para ejecutar este proyecto, necesitarás los siguientes requisitos:

- **Python 3**
- **MongoDB** (local o Atlas)
- **Bibliotecas de Python**:
  - `pymongo`

Instala los requisitos ejecutando:

```bash
pip install pymongo

Clase ChatDBManager
La clase ChatDBManager está diseñada para gestionar la base de datos ChatDB, que incluye las colecciones Carpeta y Chat.

Métodos Disponibles
1. CRUD Genérico
set_collection(collection_name): Cambia la colección activa.
create_from_json(json_file): Crea documentos desde un archivo JSON.
read_all(): Lee todos los documentos de la colección activa.
read_by_id(document_id): Lee un documento específico por su ID.
update_by_id(document_id, json_file): Actualiza un documento específico con datos de un archivo JSON.
delete_by_id(document_id): Elimina un documento específico por su ID.
2. Métodos Específicos
buscar_carpeta_por_nombre(nombre_carpeta): Busca carpetas por nombre (insensible a mayúsculas).
buscar_chats_por_correo(correo_alumno): Busca chats asociados a un correo de alumno.

Clase TareasDBManager
La clase TareasDBManager gestiona la base de datos TareasDB, que incluye las colecciones Alumno y Tarea.

Métodos Disponibles
1. CRUD Genérico
set_collection(collection_name): Cambia la colección activa.
create_from_json(json_file): Crea documentos desde un archivo JSON.
read_all(): Lee todos los documentos de la colección activa.
read_by_id(document_id): Lee un documento específico por su ID.
update_by_id(document_id, json_file): Actualiza un documento específico con datos de un archivo JSON.
delete_by_id(document_id): Elimina un documento específico por su ID.
2. Métodos Específicos
buscar_alumnos_por_calificacion(calificacion_minima): Busca alumnos con calificaciones mayores o iguales a un valor específico.

Pruebas
1. Pruebas para ChatDBManager
Ejecuta las pruebas en test_chatdb.py:
python test_chatdb.py

2. Pruebas para TareasDBManager
Ejecuta las pruebas en test_tareasdb.py:
python test_tareasdb.py