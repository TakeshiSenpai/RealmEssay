import {Box, CircularProgress} from "@mui/material"
import React, {useEffect} from "react"
import IAIcon from "./IAIcon"
import Showdown from "showdown"
import Audio from "./Audio"


// IAMessage es un componente que representa un mensaje de la inteligencia artificial
const IAMessage = ({message, doneIA}) => {

    // Función que convierte el mensaje en HTML
    const superMessage = () => {
        const conv = new Showdown.Converter()
        // Asegurarnos que los saltos de líneas y los tabs se muestren de manera correcta
        return conv.makeHtml(message.replaceAll("\\n", "<br>").replaceAll("\\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))
        // return conv.makeHtml(message)
    }

    useEffect(() => {
        console.log(message)
    }, [message])

    return (
        <Box sx={{
            display: 'flex',
            alignItems: 'flex-end',
            gap: 2,
            width: '100%',
        }}>
            <Box sx={{
                backgroundColor: (theme) => theme.palette.colors.iaBackground,
                borderRadius: '50%',
                padding: '0.5rem',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                marginRight: '0.625rem',
                offsetX: '-15px'
            }}>
                <IAIcon sx={{fill: (theme) => theme.palette.primary.main}}/>
            </Box>
            <Box sx={{
                borderRadius: '24px',
                px: '1.25rem',
                py: '.625rem',
                maxWidth: '800px',
                backgroundColor: (theme) => theme.palette.colors.iaBackground,
                whiteSpace: 'pre-wrap',
            }}
                 /*dangerouslySetInnerHTML={{__html: superMessage()}}*/
            >{message}
            </Box>
            <Box sx={{
                borderRadius: '24px',
                px: '1.25rem',
                py: '.625rem',
                backgroundColor: (theme) => theme.palette.colors.iaBackground,
            }}>
                {console.log(doneIA)}
                {!doneIA ? <CircularProgress size={30} sx={{color: (theme) => theme.palette.primary.main}}/> : <Audio
                    doneIA={doneIA}
                    message={message}
                />}
            </Box>
        </Box>
    )
}

export default IAMessage