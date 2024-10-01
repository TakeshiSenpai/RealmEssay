import { Box } from '@mui/material';
import React from 'react'
import { ComponenteDeChat } from '../components/ComponenteDeChat';


export const Home = () => {
    console.log("Estas en home");
  return (
    <Box>
        
        <ComponenteDeChat/>

    </Box>
  )
}
export default Home;