import {Box} from "@mui/material"
import React, {useEffect, useRef} from "react"
import StudentMessage from "./Chat/StudentMessage"
import IAMessage from "./Chat/IAMessage"

// Conversation es un componente que representa la conversación entre el estudiante y la IA
export function Conversation({ studentConversationArray, aIConversationArray }) {
    const conversationEndRef = useRef(null)

    // Hace scroll hasta el final de la conversación con una animación suave
    useEffect(() => {
        if (conversationEndRef.current) {
            conversationEndRef.current.scrollIntoView({ behavior: 'smooth' })
        }
    }, [studentConversationArray, aIConversationArray])

    return (
        <Box >
            {studentConversationArray.length > 0 && (
                studentConversationArray.map((mensaje, indice) => (
                    <React.Fragment key={indice}>
                        <Box sx={{ padding: 1 }} />
                        <StudentMessage message={mensaje} />
                        <Box sx={{ padding: 1 }} />
                        {aIConversationArray[indice] && <IAMessage message={aIConversationArray[indice]} />}
                    </React.Fragment>
                ))
            )}
            <div ref={conversationEndRef} />
        </Box>
    )
}

export default Conversation
