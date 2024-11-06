import {Box} from '@mui/material'

// StudentMessage es un componente que representa un mensaje del estudiante
const StudentMessage = ({ message }) => (
    <Box sx={{
        display: 'flex',
        justifyContent: 'flex-end',
        width: '100%'
    }}>
        <Box sx={{
            maxWidth: '70%',
            borderRadius: '24px',
            backgroundColor: (theme) => theme.palette.primary.main,
            px: '1.25rem',
            py: '.625rem',
            color: 'white',
            whiteSpace: "pre-line"
        }}
        >
            {message} 
        </Box>
    </Box>
)

export default StudentMessage