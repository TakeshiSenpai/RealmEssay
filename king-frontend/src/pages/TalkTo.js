import {Box} from '@mui/material'
import React, {useState} from 'react'
import {SendMessage} from '../components/Conversation/Chat/SendMessage'
import Conversation from '../components/Conversation/Conversation'
import UploadButton from "../components/Conversation/UploadButton"

//Nota: Se debe renombrar a algo relacionado a la vista del alumno y sobre enviar tarea 
//Renombrado a TalkTo como la pellicula, no se me ocurrio una mejor para describir que aqui se habla con la IA y esta responde
export const TalkTo = () => {
    const [studentConversationArray, setStudentConversationArray] = useState([])
    const [aIConversationArray, setAIConversationArray] = useState(["Mensaje de prueba, con una parte de una canción de linkin park: I'm strong on the surface Not all the way through I've never been perfect But neither have you So if you're asking me, I want you to know When my time comes Forget the wrong that I've done Help me leave behind some reasons to be missed Don't resent me And when you're feeling empty Keep me in your memory Leave out all the rest Leave out all the rest Forgetting all the hurt inside you've learned to hide so well Pretending someone else can come and save me from myself I can't be who you are When my time comes Forget the wrong that I've done Help me leave behind some reasons to be missed Don't resent me And when you're feeling empty Keep me in your memory Leave out all the rest Leave out all the rest Forgetting all the hurt inside you've learned to hide so well Pretending someone else can come and save me from myself I can't be who you are I can't be who you are "])

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
                <Conversation studentConversationArray={studentConversationArray} aIConversationArray={aIConversationArray}/>
            </Box>

            {/* Componente de chat que siempre estará en la parte inferior */}
            <Box sx={{
                padding: 2,
                marginBottom: -2
            }}>
                <SendMessage studentConversationArray={studentConversationArray} setStudentConversationArray={setStudentConversationArray}/>
            </Box>
        </Box>
    ) : <UploadButton setShowConversation={setShowConversation} />
}

export default TalkTo