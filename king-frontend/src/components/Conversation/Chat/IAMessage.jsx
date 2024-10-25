import {Box} from "@mui/material"
import React from "react"

const IAMessage = ({message}) => {
    return (
        <Box sx={{
            width: 3 / 4,
            borderRadius: 2,
            border: '2px solid black',
            padding: 1
        }}>
            {message}
        </Box>
    )
}

export default IAMessage