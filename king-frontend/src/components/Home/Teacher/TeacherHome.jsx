import Box from "@mui/material/Box"
import {Button} from "@mui/material"
import {Grading} from "@mui/icons-material"
import Typography from "@mui/material/Typography"
import {useNavigate} from "react-router-dom"
import {useIsStudent} from "../../IsStudentProvider"

const TeacherHome = () => {
    const navigate = useNavigate()
    const {isStudent, setIsStudent} = useIsStudent()

    return (
        <Box>
            <Box display="flex" justifyContent="center">
                <Button
                    variant="contained"
                    endIcon={<Grading/>}
                    onClick={() => {
                        setIsStudent(true)
                        navigate("/essays/createhomework")
                    }}
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
