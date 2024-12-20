import { Box } from "@mui/material"
import React from "react"


export function ConversationComponent({ studentConversationArray, aIConversationArray }) {

    const mostarConversacionAlumno = (mensaje) => {
        return (
            <Box
                sx={{
                    display: 'flex',
                    justifyContent: 'flex-end', // Alinea el contenido a la derecha
                    width: '100%' // Ocupa todo el ancho disponible
                }}
            >
                <Box sx={{
                    ml: 'auto',
                    maxWidth: 1 / 2,
                    display: 'inline-block',
                    borderRadius: 2,
                    border: '2px solid black',
                    padding: 1,
                    textAlign: 'rigth'
                }}>
                    {mensaje}
                </Box>
            </Box>
        )
    }

    const mostrarConversacionIA = (mensaje) => {
        return (
            <Box sx={{
                width: 3 / 4,
                borderRadius: 2,
                border: '2px solid black',
                padding: 1
            }}>
                {mensaje}
            </Box>


        )
    }
    return (

        <Box>

            {studentConversationArray.length > 0 && (studentConversationArray.map((mensaje, indice) => (
                <React.Fragment key={indice}>
                    <Box sx={{ padding: 1 }} /> {/* Espacio entre mensajes */}
                    {mostarConversacionAlumno(mensaje)}
                    <Box sx={{ padding: 1 }} /> {/* Espacio entre mensajes */}
                    {aIConversationArray[indice] && mostrarConversacionIA(aIConversationArray[indice])}

                </React.Fragment>
            )))}


        </Box>
    )

}
export default ConversationComponent