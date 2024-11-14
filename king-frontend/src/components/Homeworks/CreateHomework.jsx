import {Box, TextField, Typography} from '@mui/material'

// CreateHomework es un componente que permite al profesor crear una tarea
const CreateHomework = ({homeworkParameters, setHomeworkParameters}) => {

    // Actualiza un parámetro de la tarea
    const changeParameters = (field, value) => {
        // Actualiza el estado de homeworkParameters basado en el campo que se está editando
        setHomeworkParameters((prev) => ({
            ...prev,
            [field]: value,
        }))
    }

    return (
        <Box component="form" sx={{display: 'flex', flexDirection: 'column', gap: 2}}>
            <Typography variant="h5" component="h1" gutterBottom>
                Crear tarea
            </Typography>
            <TextField
                label="Nombre de la tarea"
                value={homeworkParameters.taskName}
                onChange={(e) => changeParameters('taskName', e.target.value)}
            />
            <TextField
                label="Descripción"
                value={homeworkParameters.description}
                onChange={(e) => changeParameters('description', e.target.value)}
                multiline
                rows={4}
            />
            <TextField
                label="Lista de estudiantes"
                value={homeworkParameters.studentList}
                onChange={(e) => changeParameters('studentList', e.target.value)}
            />
        </Box>
    )
}

export default CreateHomework
