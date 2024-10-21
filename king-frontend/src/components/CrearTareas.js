import {useEffect} from 'react'
import {TextField, Box, Typography} from '@mui/material'

const CrearTareas = ({parametrosTarea, setParametrosTarea}) => {

    const cambiarParametros = (field, value) => {
        // Actualiza el estado de parametrosTarea basado en el campo que se está editando
        setParametrosTarea((prev) => ({
            ...prev,
            [field]: value,
        }))
    }

    // Este efecto se puede usar si necesitas ejecutar algún código cuando cambian los parámetros
    useEffect(() => {
        console.log("Parametros actualizados:", parametrosTarea)
    }, [parametrosTarea])

    return (
        <Box component="form" sx={{display: 'flex', flexDirection: 'column', gap: 2}}>
            <Typography variant="h5" component="h1" gutterBottom>
                Crear tarea
            </Typography>
            <TextField
                label="Nombre de la tarea"
                value={parametrosTarea.taskName}
                onChange={(e) => cambiarParametros('taskName', e.target.value)}
            />
            <TextField
                label="Descripción"
                value={parametrosTarea.description}
                onChange={(e) => cambiarParametros('description', e.target.value)}
                multiline
                rows={4}
            />
            <TextField
                label="Lista de estudiantes"
                value={parametrosTarea.studentList}
                onChange={(e) => cambiarParametros('studentList', e.target.value)}
            />
        </Box>
    )
}

export default CrearTareas
