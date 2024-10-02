# Getting Started with Queen-Backend

Para instalar los requerimientos del proyecto:
```sh
pip install -r requirements.txt
```
## En caso de que el proyecto necesite más requerimientos
Es importante agregar el nombre de los paquetes en el archivo `requirements.txt` para que se instalen automáticamente al correr el comando `pip install -r requirements.txt`.

En caso de que hayas utilizado muchos nuevos paquetes, puedes correr el siguiente comando para actualizar el archivo `requirements.txt`:

**NOTA: ES IMPORTANTE INSTALAR LOS REQUERIMIENTOS YA EXISTENTES.**
```sh
pip freeze | cut -d "=" -f1 > requirements.txt
```

No adjuntamos la versión de los paquetes en el archivo `requirements.txt` para que haya una mayor facilidad al actualizar los paquetes.

Si tienes algún comentario/consejo que te sirvió para el desarrollo del proyecto, no dudes en agregarlo aquí.
- Agregar un comentario