import React from 'react'
import Box from "@mui/material/Box"
import Typography from "@mui/material/Typography"
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded"

// EssaysGrid es un componente que muestra los ensayos más recientes del estudiante.
const EssaysGrid = ({searchString, essays}) => {
    return (
        <Box sx={{
            display: "flex",
            overflowX: "auto",
            padding: 1,
            gap: 2,
        }}>
            {essays
                .filter(essay =>
                    essay.title.toLowerCase().includes(searchString.toLowerCase()) ||
                    essay.subject.toLowerCase().includes(searchString.toLowerCase())
                )
                .sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate))
                .map((essay, index) => {
                    const mainColorString = essay.completed ? "green" : new Date(essay.dueDate) < new Date() ? "red" : "gray"
                    const mainColor = mainColorString === 'red' ? "rgba(255, 0, 0, 0.1)" : mainColorString === 'green' ? "rgba(0, 255, 0, 0.1)" : "rgba(128, 128, 128, 0.1)"

                    return (
                        <Box key={index} sx={{
                            width: 300,
                            minWidth: 300,
                            height: 300,
                            borderRadius: 3,
                            border: 2,
                            borderColor: mainColor,
                            backgroundColor: mainColor,
                            display: "flex",
                            flexDirection: "column",
                            padding: 1
                        }}>
                            <Typography variant="h6" fontWeight="800">
                                {essay.title}
                            </Typography>

                            <Typography>
                                {essay.subject}
                            </Typography>

                            <Box sx={{flex: 1}}></Box>

                            {essay.completed && (
                                <Typography
                                    sx={{
                                        fontWeight: 'bold',
                                        background: mainColor,
                                        padding: 1,
                                        borderRadius: 1,
                                        display: "flex"
                                    }}
                                >
                                    Ensayo entregado <span style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 5
                                }}> <CheckCircleRoundedIcon/> </span>
                                </Typography>
                            )}

                            <Typography
                                sx={{
                                    fontWeight: 'bold',
                                    background: mainColorString === 'red' ? "rgba(255, 0, 0, 0.1)" : "transparent",
                                    padding: 1,
                                    borderRadius: 1,
                                }}
                            >
                                Fecha de entrega: <span style={{
                                fontWeight: 'bold',
                                color: mainColorString === 'red' ? 'red' : 'inherit'
                            }}>{new Date(essay.dueDate).toLocaleDateString()} </span>
                            </Typography>
                        </Box>
                    )
                })}
        </Box>
    )
}

export default EssaysGrid