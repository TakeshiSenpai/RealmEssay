import {Box} from "@mui/material"
import React from "react"
import IAIcon from "./IAIcon"
import Showdown from "showdown"


const IAMessage = ({message})  =>{
    const superMessage = ()=>{
        const conv = new Showdown.Converter()
        //Nose porque el \n no lo convierte a br, por lo que se debe aplicar ese replace
        return conv.makeHtml(message.replaceAll("\\n", "<br>").replaceAll("\\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))
        
         
    }
    return(
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
        dangerouslySetInnerHTML={{ __html: superMessage() }}>
             
        </Box>
    </Box>)
        }

export default IAMessage