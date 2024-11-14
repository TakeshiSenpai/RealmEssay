import Box from "@mui/material/Box"
import Typography from "@mui/material/Typography"
import {useNavigate} from "react-router-dom"
import {Add, Grading} from "@mui/icons-material"
import EssaysGrid from "./EssaysGrid"
import {Button} from "@mui/material"
import IconButton from "@mui/material/IconButton"
import HomeworkCode from "../../Homeworks/HomeworkCode"
import {useState} from "react"

const StudentEssays = ({searchString, essays}) => {
    const [openHomeworkCodeModal, setOpenHomeworkCodeModal] = useState(false)
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
                <span>
                    <IconButton sx={{marginLeft: 1}} onClick={() => setOpenHomeworkCodeModal(true) }>
                        <Add/>
                    </IconButton>
                </span>
            </Typography>

            <EssaysGrid searchString={searchString} essays={essays}/>

            <HomeworkCode openModal={openHomeworkCodeModal} setOpenModal={setOpenHomeworkCodeModal} addToConversationArray={(code) => {}} />
        </Box>
    )
}

export default StudentEssays