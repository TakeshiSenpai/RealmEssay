# Getting Started with Queen-Backend

## Agregar queen-backend a las carpetas del intérprete de Python
Para poder correr el proyecto, es necesario agregar la carpeta `queen-backend` a las carpetas del intérprete de Python.

### Instrucciones

#### PyCharm (probadas)
1. Haz clic derecho en la carpeta queen-backend.
Selecciona Mark Directory as > Sources Root.
2. Ve a File > Settings (o PyCharm > Preferences en macOS). 
3. Navega a Project > Python Interpreter. 
4. Da clic en el dropdown menu de los interpretes y selecciona Show All... 
5. Selecciona tu intérprete en la lista izquierda y haz clic en el icono de Show Interpreter Paths. 
6. Añade la carpeta raíz queen-backend haciendo clic en el botón de + y selecciona la carpeta.

#### Visual Studio Code (no probadas, si las prueban, por favor confirmen si funcionan, si no, por favor, indiquen qué pasos faltan)
1. Presiona Ctrl + Shift + P (o Cmd + Shift + P en macOS) para abrir la paleta de comandos.
2. Escribe y selecciona Preferences: Open Settings (JSON). Si no ves esta opción, puedes buscar el archivo directamente en la estructura de carpetas del proyecto bajo .vscode/settings.json. 
3. Si el archivo no existe, VSCode creará uno. Añade o edita las siguientes líneas:
    ```json
    {
        "python.autoComplete.extraPaths": [
            "./queen-backend"
        ],
        "python.analysis.extraPaths": [
            "./queen-backend"
        ]
    }
    ```
4. Reiniciar VSCode.

## Requerimientos

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