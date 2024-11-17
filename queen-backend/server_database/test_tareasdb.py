from tareasdb_manager import TareasDBManager

# Inicializar la clase
tareas_db = TareasDBManager()

# Seleccionar la colección 'Alumno'
tareas_db.set_collection("Alumno")

# Crear documentos en la colección 'Alumno'
print("Creando documentos en la colección 'Alumno'...")
tareas_db.create_from_json("alumnos.json")

# Leer todos los documentos en la colección 'Alumno'
print("\nLeyendo todos los documentos en la colección 'Alumno'...")
tareas = tareas_db.read_all()

# Leer un documento específico por su ID
if tareas:
    primer_id = tareas[0]['_id']
    print(f"\nLeyendo documento con ID: {primer_id}...")
    tareas_db.read_by_id(primer_id)

# Actualizar un documento por su ID
print("\nActualizando el primer documento...")
tareas_db.update_by_id(primer_id, "actualizacion_alumno.json")

# Eliminar un documento por su ID
print("\nEliminando el primer documento...")
tareas_db.delete_by_id(primer_id)

# Buscar alumnos con calificación >= 90
print("\nBuscando alumnos con calificación >= 90...")
tareas_db.buscar_alumnos_por_calificacion(90)
