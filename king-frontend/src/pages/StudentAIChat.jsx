import {Box} from '@mui/material'
import React, {useState} from 'react'
import SendMessage from '../components/Conversation/Chat/SendMessage'
import Conversation from '../components/Conversation/Conversation'
import UploadButton from "../components/Conversation/UploadButton"

// StudentAIChat es un componente que representa la vista del chat del alumno con la IA
const StudentAIChat = () => {
    const [studentConversationArray, setStudentConversationArray] = useState([])
    const [aIConversationArray, setAiConversationArray] = useState([])

    const [showConversation, setShowConversation] = useState(false)

    return showConversation ? (
        <Box sx={{
            display: 'flex',
            flexDirection: 'column',
            height: '95vh'
        }}>
            {/* Componente que muestra las conversaciones */}
            <Box sx={{
                flexGrow: 1,
                overflowY: 'auto',  // Permite el scroll si el contenido excede el tamaño
                paddingY: 4,
                paddingX: 2,
            }}>
                <Conversation 
                    studentConversationArray={studentConversationArray} 
                    aIConversationArray={aIConversationArray}
                />
            </Box>

            {/* Componente de chat que siempre estará en la parte inferior */}
            <Box sx={{
                padding: 2,
                marginBottom: -2
            }}>
                <SendMessage 
                    studentConversationArray={studentConversationArray} 
                    setStudentConversationArray={setStudentConversationArray}
                    aIConversationArray={aIConversationArray}
                    setAiConversationArray={setAiConversationArray}
                />
            </Box>
        </Box>
    ) : <UploadButton setShowConversation={setShowConversation} />
}

export default StudentAIChat