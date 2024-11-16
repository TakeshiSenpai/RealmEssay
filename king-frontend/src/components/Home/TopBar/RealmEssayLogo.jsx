import IAIcon from "../../Conversation/Chat/IAIcon";
import {createTheme, ThemeProvider} from "@mui/material";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import React from "react";

// RealmEssayLogo es un componente que representa el logo de RealmEssay
const RealmEssayLogo = () => {
    // Tipografía serif para la parte de 'Realm'
     const serifTheme = createTheme({
        typography: {
            fontFamily: 'Mea Culpa',
        },
    })

    return (
        <Box
            sx={{
                position: 'relative',
                alignItems: 'center',
                display: 'flex',
                padding: '5px',

                '&::before': {
                    content: '""',
                    position: 'absolute',
                    inset: 0,
                    borderRadius: '10px',
                    padding: '2px',
                    background: (theme) => theme.palette.colors.textGradient,
                    WebkitMask: `linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)`,
                    WebkitMaskComposite: 'xor',
                    maskComposite: 'exclude',
                    zIndex: -1,
                },
            }}
        >
            <IAIcon sx={{
                fill: (theme) => theme.palette.primary.main,
                marginLeft: '5px',
            }}/>
            <ThemeProvider theme={serifTheme}>
                <Typography variant="h4" style={{fontSize: '1.6rem'}}>
                    Realm
                </Typography>
            </ThemeProvider>
            <Typography
                variant="h4"
                style={{
                    fontSize: '1.5rem',
                    fontWeight: 'bold',
                    marginRight: '5px'
                }}
            >
                Essay
            </Typography>
        </Box>
    )
}

export default RealmEssayLogo