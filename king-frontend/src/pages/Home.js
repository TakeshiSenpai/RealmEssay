import { Box } from '@mui/material';
import React from 'react'
import { ChatComponent } from '../components/ChatComponent';

export const Home = () => {
    console.log("Estas en home")
    return (
        <Box>
            <ChatComponent/>
        </Box>
    )
}

export default Home