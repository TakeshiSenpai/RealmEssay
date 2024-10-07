import * as React from 'react'
import Button from '@mui/joy/Button'
import Textarea from '@mui/joy/Textarea'
import {Box} from '@mui/joy'
import { AttachFile, Send } from '@mui/icons-material'
import { Navigate } from 'react-router-dom'
import { styled } from '@mui/joy';
import { IconButton } from '@mui/material'

export const ComponenteDeChat = () => {
    const token = localStorage.getItem('token') 

    const [mensaje,setMensaje] = React.useState('')
    const handleChange = (event) => {
        setMensaje(event.target.value) // Actualiza el estado con el valor actual
      }
      const handleSubmit = () => {
        console.log("Mensaje escrito:", mensaje) // Aquí podrías hacer algo con el mensaje, como enviarlo a una API
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
        display: 'flex',          // Usar flexbox
        flexDirection: 'column',  // Disposición en columna
        minHeight: '91vh'       // Ocupa al menos toda la altura de la ventana
      }}
    >
      <Box sx={{ flexGrow: 1 }} /> {/* Este Box vacío empuja el siguiente contenido hacia abajo */}
      
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
        <VisuallyHiddenInput type="file" accept=".pdf"/>
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
    </Box>
      
  ) : <Navigate to="/auth" />
}
