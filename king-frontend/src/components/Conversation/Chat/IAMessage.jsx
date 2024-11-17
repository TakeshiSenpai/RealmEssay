import {Box} from "@mui/material"
import React from "react"
import IAIcon from "./IAIcon"
import Showdown from "showdown"

// IAMessage es un componente que representa un mensaje de la inteligencia artificial
const IAMessage = ({message}) => {
    
    // Función que convierte el mensaje en HTML
    const superMessage = () => {
        const conv = new Showdown.Converter()
        // Asegurarnos que los saltos de líneas y los tabs se muestren de manera correcta
        //return conv.makeHtml(message.replaceAll("\\n", "<br>").replaceAll("\\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))
        return conv.makeHtml(message)
    }

    return (
        <Box sx={{
            display: 'flex',
            alignItems: 'flex-end',
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
                backgroundColor: (theme) => theme.palette.colors.iaBackground,
                whiteSpace: 'pre-wrap',
            }}
                 dangerouslySetInnerHTML={{__html: superMessage()}}>
            </Box>
        </Box>)
}

export default IAMessage