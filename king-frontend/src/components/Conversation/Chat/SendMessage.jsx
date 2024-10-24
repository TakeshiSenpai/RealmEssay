import * as React from 'react'
import {useState} from 'react'
import {Box, IconButton, TextField} from '@mui/material'
import {Send} from '@mui/icons-material'
import {Navigate} from 'react-router-dom'

export const SendMessage = ({studentConversationArray, setStudentConversationArray}) => {

    const token = localStorage.getItem('token')

    const [message, setMessage] = useState('')
    const handleChange = (event) => {
        setMessage(event.target.value) // Actualiza el estado con el valor actual
    }

    const handleSubmit = async () => {
        //Aqui se deberia habla con la IA y que por aqui responda
        setStudentConversationArray([...studentConversationArray, message])
        setMessage("")
        //Tambien debe como que inhabilitar el chat hasta que la IA conteste como un spiner
    }

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
                sx={{
                    ml: 'auto',
                    color: (theme) => theme.palette.primary.main
                }}
                disabled={!message.trim()}
            >
                <Send/>
            </IconButton>
        </Box>
    ) : <Navigate to="/auth"/>
}

export default SendMessage