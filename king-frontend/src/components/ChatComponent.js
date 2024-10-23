import * as React from 'react'
import {Box, IconButton, TextField} from '@mui/material'
import {AttachFile, Send} from '@mui/icons-material'
import {Navigate} from 'react-router-dom'
import {styled} from '@mui/joy';

export const ChatComponent = ({studentConversationArray, setStudentConversationArray}) => {

    const token = localStorage.getItem('token')

    const [message, setMessage] = React.useState('')
    const handleChange = (event) => {
        
        setMessage(event.target.value) // Actualiza el estado con el valor actual
    }
    

    const handleSubmit = async () => {
        //Aqui se deberia habla con la IA y que por aqui responda
        setStudentConversationArray ([...studentConversationArray, message])
        setMessage("")
        //Tambien debe como que inhabilitar el chat hasta que la IA conteste como un spiner
                

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
                padding: '0',
                marginBottom: '-10px'
            }}
        >
            {/* Botón a la izquierda el de subir el pdf, es decir el "clip" */}
            <IconButton
                variant="outlined"
                component="label"
                role={undefined}
                tabIndex={-1}
                sx={{mb: 'auto'}} // Ajustar la altura del botón
            >
                <AttachFile/>
                <VisuallyHiddenInput type="file" accept=".pdf, .txt"/>
            </IconButton>

            {/* Área de texto en el centro, aqui se habla con la IA */}
            <TextField
                multiline
                maxRows={4}
                placeholder="Escribe aquí..."
                variant="outlined"
                value={message} // El valor del TextArea viene del estado
                onChange={handleChange} // Cada vez que el usuario escribe, se ejecuta esta función
                fullWidth
                sx={{flexGrow: 1}}  // El área de texto toma el espacio restante
            />

            {/* Botón a la derecha, es el boton de envio, probablemente aqui deberia ir el spiner*/}
            <IconButton
                variant="outlined"
                onClick={handleSubmit}
                sx={{ml: 'auto'}}
            >
                <Send/>
            </IconButton>
        </Box>


    ) : <Navigate to="/auth"/>
}
