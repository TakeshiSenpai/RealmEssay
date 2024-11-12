import * as React from 'react'
import {useEffect, useState} from 'react'
import {Box, CircularProgress, IconButton, TextField} from '@mui/material'
import {Send} from '@mui/icons-material'
import {Navigate} from 'react-router-dom'
import Showdown from 'showdown'

// SendMessage es un componente que permite al estudiante enviar mensajes a la IA
const SendMessage = ({
                                studentConversationArray,
                                setStudentConversationArray,
                                aIConversationArray,
                                setAiConversationArray
                            }) => {
    const token = localStorage.getItem('token')
    const [message, setMessage] = useState('')
    const [loading, setLoading] = useState(false)  // Nuevo estado para controlar el spinner
    const IAUrl = process.env.VERCEL_IA
                ? `https://${process.env.VERCEL_IA}`
                : 'http://127.0.0.1:2003'
    // Actualiza el estado con el valor actual del TextField
    const handleChange = (event) => {
        setMessage(event.target.value)
    }

    // Enviar el mensaje a la IA
    const handleSubmit = async () => {
        // Agrega el mensaje del estudiante a la conversación
        setStudentConversationArray([...studentConversationArray, message])
        setMessage('')
        setLoading(true) // Activar el spinner cuando se envía el mensaje
        
        try {
            const response = await fetch(`${IAUrl}/questions_and_responses`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({student_questions: [message]})
            })
            if (response.ok) {
                const reader = response.body.getReader()
                const decoder = new TextDecoder('utf-8')
                let done = false
                let accumulatedText = ""

                while (!done) {
                    const {value, done: streamDone} = await reader.read()
                    console.log(value, done)
                    done = streamDone
                    if (value) {
                        const chunk = decoder.decode(value, {stream: true})
                        accumulatedText += chunk
                        
                        // Actualizar el array con el nuevo fragmento
                        setAiConversationArray([...aIConversationArray, accumulatedText])
                    }
                }
            } else {
                console.error(`Error: ${response.status} - ${response.statusText}`)
            }
        } catch (error) {
            console.error('Error durante la recepción de la respuesta de la IA:', error)
        }
        setLoading(false)  // Desactivar el spinner al finalizar la solicitud o en caso de error
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
            <TextField
                multiline
                maxRows={4}
                placeholder="Escribe tu comentario o pregunta sobre el ensayo..."
                variant="outlined"
                value={message}
                onChange={handleChange}
                fullWidth
                sx={{
                    flexGrow: 1,
                    borderRadius: '24px',
                    backgroundColor: (theme) => theme.palette.colors.iaBackground,
                    '& .MuiOutlinedInput-root': {
                        borderRadius: '24px',
                    },
                }}
                disabled={loading}  // Desactiva el TextField mientras se espera la respuesta
            />

            {loading ? (
                <CircularProgress size={30} sx={{color: (theme) => theme.palette.primary.main}}/>
            ) : (
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
            )}
        </Box>
    ) : (
        <Navigate to="/auth"/>
    )
}

export default SendMessage
