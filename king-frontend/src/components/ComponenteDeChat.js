import * as React from 'react'
import Button from '@mui/joy/Button'
import Textarea from '@mui/joy/Textarea'
import {Box} from '@mui/joy'
import { AttachFile, Send } from '@mui/icons-material'
import { Navigate } from 'react-router-dom'

export const ComponenteDeChat = () => {
    const token = localStorage.getItem('token') 

    const [mensaje,setMensaje] = React.useState('')
    const handleChange = (event) => {
        setMensaje(event.target.value) // Actualiza el estado con el valor actual
      }
      const handleSubmit = () => {
        console.log("Mensaje escrito:", mensaje) // Aquí podrías hacer algo con el mensaje, como enviarlo a una API
      }



  return token ? (
    <Box 
      sx={{ 
        display: 'flex',          // Usar flexbox
        flexDirection: 'column',  // Disposición en columna
        minHeight: '90vh'       // Ocupa al menos toda la altura de la ventana
      }}
    >
      <Box sx={{ flexGrow: 1 }} /> {/* Este Box vacío empuja el siguiente contenido hacia abajo */}
      
      <Box 
      sx={{ 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center', 
        gap: '10px', // Espacio entre los elementos
        padding: '20px'
      }}
    >
      {/* Botón a la izquierda */}
      <Button 
        variant="outlined" 
        color="primary" 
        sx={{ mb:'auto' }} // Ajustar la altura del botón
      >
        <AttachFile/> 
      </Button>

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
      <Button 
        variant="outlined" 
        color="primary" 
        onClick={handleSubmit}
        sx={{ mb:'auto' }}      
        >
        <Send/>
      </Button>
    </Box>
    </Box>
      
  ) : <Navigate to="/auth" />
}