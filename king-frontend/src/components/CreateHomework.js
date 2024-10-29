import {useEffect} from 'react'
import {Box, TextField, Typography} from '@mui/material'

const CreateHomework = ({homeworkParameters, setHomeworkParameters}) => {

    const cambiarParametros = (field, value) => {
        // Actualiza el estado de homeworkParameters basado en el campo que se está editando
        setHomeworkParameters((prev) => ({
            ...prev,
            [field]: value,
        }))
    }

    // Este efecto se puede usar si necesitas ejecutar algún código cuando cambian los parámetros
    useEffect(() => {
        console.log("Parametros actualizados:", homeworkParameters)
    }, [homeworkParameters])

    return (
        <Box component="form" sx={{display: 'flex', flexDirection: 'column', gap: 2}}>
            <Typography variant="h5" component="h1" gutterBottom>
                Crear tarea
            </Typography>
            <TextField
                label="Nombre de la tarea"
                value={homeworkParameters.taskName}
                onChange={(e) => cambiarParametros('taskName', e.target.value)}
            />
            <TextField
                label="Descripción"
                value={homeworkParameters.description}
                onChange={(e) => cambiarParametros('description', e.target.value)}
                multiline
                rows={4}
            />
            <TextField
                label="Lista de estudiantes"
                value={homeworkParameters.studentList}
                onChange={(e) => cambiarParametros('studentList', e.target.value)}
            />
        </Box>
    )
}

export default CreateHomework
