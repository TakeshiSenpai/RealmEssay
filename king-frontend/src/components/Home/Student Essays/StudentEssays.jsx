import Box from "@mui/material/Box"
import Typography from "@mui/material/Typography"
import {useNavigate} from "react-router-dom"
import {Grading} from "@mui/icons-material"
import EssaysGrid from "./EssaysGrid";
import {Button} from "@mui/material";

const StudentEssays = ({searchString, essays}) => {
    const navigate = useNavigate()

    return (
        <Box>
            <Box display="flex" justifyContent="center">
                <Button
                    variant="contained"
                    endIcon={<Grading/>}
                    onClick={() => navigate("/essays")}
                >
                    <Typography fontWeight="bold" textTransform="none">
                        Ver todos los ensayos y ChatBot
                    </Typography>
                </Button>
            </Box>

            <Typography variant="h5" marginY={2} color="gray" fontWeight="bold">
                Ensayos recientes
            </Typography>

            <EssaysGrid essays={essays}/>
        </Box>
    )
}

export default StudentEssays