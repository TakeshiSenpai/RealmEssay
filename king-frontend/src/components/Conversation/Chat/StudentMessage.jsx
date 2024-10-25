import {Box} from "@mui/material"
import React from "react"

const StudentMessage = ({message}) => {
    return (
        <Box sx={{
            display: 'flex',
            justifyContent: 'flex-end', // Alinea el contenido a la derecha
            width: '100%' // Ocupa todo el ancho disponible
        }}>
            <Box sx={{
                ml: 'auto',
                maxWidth: 1 / 2,
                display: 'inline-block',
                borderRadius: 2,
                border: '2px solid black',
                padding: 1,
                textAlign: 'rigth'
            }}>
                {message}
            </Box>
        </Box>
    )
}

export default StudentMessage