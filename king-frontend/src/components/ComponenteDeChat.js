import * as React from 'react'
import Button from '@mui/joy/Button'
import Textarea from '@mui/joy/Textarea'
import {Box} from '@mui/joy'
import { AttachFile, Send } from '@mui/icons-material'
import { Navigate } from 'react-router-dom'
import { styled } from '@mui/joy';
import { IconButton } from '@mui/material'

export const ComponenteDeChat = ({arregloDeConversacionAlumno, setArregloDeConversacionAlumno}) => {

    const token = localStorage.getItem('token') 

    const [mensaje,setMensaje] = React.useState('')
    const handleChange = (event) => {
        setMensaje(event.target.value) // Actualiza el estado con el valor actual
      }
      const handleSubmit = async () => {
        const rubricaPrueba =  "Se te presenta la rúbrica para evaluar el ensayo. Consta de 2 parámetros, cada uno con un título, descripción, valor máximo y un conjunto de niveles de desempeño (criterios). Cada nivel tiene una descripción y un puntaje asociado. Selecciona el nivel de desempeño más adecuado para cada parámetro del ensayo. Al final, deberás presentar el puntaje total, indicando el puntaje de cada parámetro y proporcionando una breve justificación. Parámetro 1: Ortografia"+"Descripción: Se revisara el trabajao con respecto a palabras bien escritas y que tengan acento donde deberian Valor total: 40 Criterios: Criterio 1: Si no tiene ninguno entonces no hay puntos que restar Valor parcial: 40 Criterio 2: Si tiene 4 faltas de ortografia deberia ser 0 en este parametro, es decir, - 40 puntos Valor parcial: 0"
+"Parámetro 2: Contenido"
+ "Descripción: En el contenido habla sobre el creador del rubik y la importancia del cubo"
+"Valor total: 60"
+"Criterios:"
+	"Criterio 1: Si tiene los dos contenidos solicitados, es decir el creador y la importancia entinces es todos los puntos"
+	"Valor parcial: 60"
+"	Criterio 2: SOlo habla del autor o de la importancia del rubik es la mitad de puntos"
+	"Valor parcial: 30"
+	"Criterio 3: Si no habla de ninguno entonces es 0"
+"	Valor parcial: 0"

        console.log("Mensaje escrito:", mensaje) // Aquí podrías hacer algo con el mensaje, como enviarlo a una API
        const response = await fetch('http://127.0.0.1:5000/submit', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({input: mensaje})
      })


      var data = await response.json()
      console.log(data)
      const response2 = await fetch('http://127.0.0.1:5000/submit_criteria', {
        method: 'POST', headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({criteria: rubricaPrueba})})
        data =await response2.json()
        console.log(data)

      const response3 =  await fetch('http://127.0.0.1:5000/response', {
        method: 'GET', headers:{
          'Content-Type': 'application/json'
        } })

        data = response3
        console.log(data)
      
        setMensaje("")
        setArregloDeConversacionAlumno([...arregloDeConversacionAlumno,mensaje])
      
      }

      const VisuallyHiddenInput = styled('input')`
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  bottom: 0;
  left: 0;
  white-space: nowrap;
  width: 1px;
`;

  return token ? (
    
     
      <Box 
      sx={{ 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
        gap: '10px', // Espacio entre los elementos
        padding: '0px'
      }}
    >
      {/* Botón a la izquierda */}
      <IconButton 
        variant="outlined"  
        component="label"
        role={undefined}
        tabIndex={-1}
        sx={{ mb:'auto' }} // Ajustar la altura del botón
      >
        <AttachFile/> 
        <VisuallyHiddenInput type="file" accept=".pdf, .txt"/>
      </IconButton>

      {/* Área de texto en el centro */}
      <Textarea
        multiline
        maxRows={4}
        placeholder="Escribe aquí..."
        variant="outlined"
        value={mensaje} // El valor del TextArea viene del estado
        onChange={handleChange} // Cada vez que el usuario escribe, se ejecuta esta función
        fullWidth
        sx={{ flexGrow: 1 }}  // El área de texto toma el espacio restante
      />

      {/* Botón a la derecha */}
      <IconButton 
        variant="outlined" 
        onClick={handleSubmit}
        sx={{ ml:'auto' }}      
        >
        <Send/>
      </IconButton>
    </Box>
    
      
  ) : <Navigate to="/auth" />
}
