import { Box } from '@mui/material';
import React from 'react'
import { ComponenteDeChat } from '../components/ComponenteDeChat';
import ComponenteDeConversacion from'../components/ComponenteDeConversacion';


//Nota: Se debe renombrar a algo relacionado a la vista del alumno y sobre enviar tarea 
export const Home = () => {
  const [mensajeIA,setMensajeIA] =  React.useState("")
  const [arregloDeConversacionAlumno,setArregloDeConversacioensAlumno] = React.useState([])
  const [arregloDeConversacionIA, setArregloDeConversacionIA] = React.useState(["Mensaje de prueba, con una parte de una canción de linkin park: I'm strong on the surface Not all the way through I've never been perfect But neither have you So if you're asking me, I want you to know When my time comes Forget the wrong that I've done Help me leave behind some reasons to be missed Don't resent me And when you're feeling empty Keep me in your memory Leave out all the rest Leave out all the rest Forgetting all the hurt inside you've learned to hide so well Pretending someone else can come and save me from myself I can't be who you are When my time comes Forget the wrong that I've done Help me leave behind some reasons to be missed Don't resent me And when you're feeling empty Keep me in your memory Leave out all the rest Leave out all the rest Forgetting all the hurt inside you've learned to hide so well Pretending someone else can come and save me from myself I can't be who you are I can't be who you are "])
  return (
    <Box sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      height: '91vh'  // Ocupa todo el alto de la pantalla
  }}>
    {/* Componente que muestra las conversaciones */}
    <Box sx={{ 
        flexGrow: 1, 
        overflowY: 'auto',  // Permite el scroll si el contenido excede el tamaño
        paddingY: 4, 
        paddingX: 2,  
    }}>
      <ComponenteDeConversacion arregloDeConversacionAlumno={arregloDeConversacionAlumno} arregloDeConversacionIA={arregloDeConversacionIA} />
    </Box>

    {/* Componente de chat que siempre estará en la parte inferior */}
    <Box sx={{ 
        borderTop: '1px solid #ddd', 
        padding: 2 
    }}>
      <ComponenteDeChat arregloDeConversacionAlumno={arregloDeConversacionAlumno} setArregloDeConversacionAlumno= {setArregloDeConversacioensAlumno} />
    </Box>
  </Box>

  )
}
export default Home;