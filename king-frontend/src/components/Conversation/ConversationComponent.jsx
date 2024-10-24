import {Box} from "@mui/material"
import React from "react"
import StudentMessage from "./Chat/StudentMessage";
import IAMessage from "./Chat/IAMessage";


export function ConversationComponent({studentConversationArray, aIConversationArray}) {
    return (
        <Box>
            {studentConversationArray.length > 0 && (studentConversationArray.map((mensaje, indice) => (
                <React.Fragment key={indice}>
                    <Box sx={{padding: 1}}/>
                    <StudentMessage message={mensaje}/>
                    <Box sx={{padding: 1}}/>
                    {aIConversationArray[indice] && <IAMessage message={aIConversationArray[indice]}/>}
                </React.Fragment>
            )))}
        </Box>
    )
}

export default ConversationComponent