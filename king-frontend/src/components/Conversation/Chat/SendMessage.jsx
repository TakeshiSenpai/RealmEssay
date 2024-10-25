import * as React from 'react'
import {useEffect, useState} from 'react'
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
        // Aquí se debería hablar con la IA y que por aquí responda
        setStudentConversationArray([...studentConversationArray, message])
        setMessage('')
        // También debe inhabilitar el chat hasta que la IA conteste como un spinner
    }

    // Enviar el mensaje al presionar `Ctrl (Command) + Enter`
    useEffect(() => {
        const handleKeyDown = async (event) => {
            if ((event.key === 'Enter' && (event.metaKey || event.ctrlKey)) && message.trim()) {
                event.preventDefault()
                await handleSubmit()
            }
        }

        window.addEventListener('keydown', handleKeyDown)
        return () => window.removeEventListener('keydown', handleKeyDown)
    }, [message, studentConversationArray])

    return token ? (
        <Box
            sx={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '10px', // Espacio entre los elementos
                padding: '0',
                marginBottom: '-10px',
            }}
        >
            {/* Área de texto en el centro, aquí se habla con la IA */}
            <TextField
                multiline
                maxRows={4}
                placeholder="Escribe tu comentario o pregunta sobre el ensayo..."
                variant="outlined" // Usamos outlined en vez de filled porque filled tiene una alineación rara
                value={message} // El valor del TextArea viene del estado
                onChange={handleChange} // Cada vez que el usuario escribe, se ejecuta esta función
                fullWidth
                sx={{
                    flexGrow: 1,
                    borderRadius: '24px',
                    backgroundColor: (theme) => theme.palette.colors.iaBackground,
                    '& .MuiOutlinedInput-root': {
                        borderRadius: '24px',
                    },
                }}
            />

            {/* Botón a la derecha, es el botón de envío, probablemente aquí debería ir el spinner */}
            <IconButton
                variant="outlined"
                onClick={handleSubmit}
                sx={{
                    ml: 'auto',
                    color: (theme) => theme.palette.primary.main,
                }}
                disabled={!message.trim()}
            >
                <Send/>
            </IconButton>
        </Box>
    ) : (
        <Navigate to="/auth"/>
    )
}

export default SendMessage