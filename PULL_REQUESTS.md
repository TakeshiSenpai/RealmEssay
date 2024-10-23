# Proceso de revisión de Pull Requests

Si estás aquí, es porque vas a revisar un Pull Request. ¡Felicidades. Eres alguien importante en el equipo (a.k.a Todos)! 🎉

Es importante probar el código antes de aprobar un Pull Request, con esto evitamos una catástrofe. Para hacerlo, sigue los siguientes pasos:

1. **Clona el repositorio** en tu máquina local.
   - Este clone debe ser distinto al que ya tienes en tu computadora, usa este nuevo clone **exclusivamente para revisar Pull Requests**. 
```bash
git clone https://github.com/TakeshiSenpai/RealmEssay 
```
2. **Instala las dependencias** del proyecto.
   - Ver `README.md` del [**king-frontend**](king-frontend/README.md) y del [**queen-backend**](queen-backend/README.md) para más información.

3. **Obtén el #** del Pull Request que deseas revisar.

4. **Cambia a la rama** del Pull Request.
   - Reemplaza `#` por el número del Pull Request.
```bash
git fetch origin pull/#/head && git checkout FETCH_HEAD
```

5. En caso de que se requieran cambios, una vez actualizado el pull request en Github, para actualizar la rama local, vuelve a ejecutar el comando del paso 4. 

## Criterios de aceptación

1. **Cumplimiento de la convención de código**.
   - Ver [**convención de código**](CODE_CONVENTION.md) para más información.
     - `Apréndansela, apliquénla, vivánla, aménla, conviértanse en ella. La convención es ustedes, y ustedes son la convención. La convención es el camino, la verdad y la vida. Sin la convención, son nada.`
2. El pull request **debe correr sin errores en tu computadora**.