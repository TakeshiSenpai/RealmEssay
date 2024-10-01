import { useState } from "react"
import React from 'react' //Para crear componentes en react, devuelve un trozo de htlm 

//Para crear todo de golpe usar "   "
export const NuevoComponente = () => {

    const [nombre,SuperNombre] = useState("Enrique")
    //Const [nombre de la variable, metodo usado para cambiar] = usestate( El valor por defecto);
    const cambiarNombre =(nuevoNombre) => {

        SuperNombre(nuevoNombre);
    }
  return (
    <div>Hola como estas te ved bien eh. Mi nombre es {nombre}
    Ahora con color<strong className={nombre.length >7 ? 'rojo': "azul"} > {nombre}</strong>
        <button onClick= { e=> cambiarNombre("FelipePunks")}>   
            Cambiar nombre 
        </button>
    </div>

      )
}