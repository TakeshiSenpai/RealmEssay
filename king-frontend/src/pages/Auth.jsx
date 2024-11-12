import {Box, createTheme, ThemeProvider} from '@mui/material'
import React from 'react'
import GoogleButton from '../components/GoogleButton'
import Typography from "@mui/material/Typography";
import IAIcon from "../components/Conversation/Chat/IAIcon";

// Auth es un componente que representa la página de autenticación
const Auth = () => {

    // Tema personalizado para el texto
    const theme = createTheme({
        typography: {
            fontFamily: 'Mea Culpa',
        },
    })

    return (
        <Box
            display="flex"
            flexDirection="column"
            alignItems="center"
            justifyContent="center"
            height="100vh"
        >
            <Box display="flex" alignItems="center">
                <IAIcon sx={{
                    fill: (theme) => theme.palette.primary.main,
                }}/>
                <ThemeProvider theme={theme}>
                    <Typography variant="h1" style={{fontSize: '4rem'}}>
                        Realm
                    </Typography>
                </ThemeProvider>
                <Typography
                    variant="h1"
                    style={{
                        fontSize: '3rem',
                        fontWeight: 'bold',
                        marginLeft: '5px',
                        marginBottom: '-10px'
                    }}
                >
                    Essay
                </Typography>
            </Box>

            <Typography
                style={{
                    fontSize: '2rem',
                    textAlign: 'center',
                    margin: '20px 0',
                    fontWeight: 600
                }}
            >
                Revisión de ensayos impulsada por <Typography component='span' sx={{
                background: (theme) => theme.palette.colors.textGradient,
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                fontSize: '2rem',
                fontWeight: 600
            }}>Inteligencia Artificial</Typography>.
            </Typography>

            <GoogleButton/>
        </Box>
    )
}

export default Auth
