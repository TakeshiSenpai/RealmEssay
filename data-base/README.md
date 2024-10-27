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
