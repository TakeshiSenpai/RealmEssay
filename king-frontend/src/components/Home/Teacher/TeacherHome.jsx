import Box from "@mui/material/Box"
import {Button} from "@mui/material"
import {Grading} from "@mui/icons-material"
import Typography from "@mui/material/Typography"
import {useNavigate} from "react-router-dom"

const TeacherHome = () => {
    const navigate = useNavigate()
    return (
        <Box>
            <Box display="flex" justifyContent="center">
                <Button
                    variant="contained"
                    endIcon={<Grading/>}
                    onClick={() => navigate("/essays/createhomework")}
                >
                    <Typography fontWeight="bold" textTransform="none">
                        Crear nueva tarea
                    </Typography>
                </Button>
            </Box>
        </Box>
    )
}

export default TeacherHome