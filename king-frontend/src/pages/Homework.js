import React from 'react'
import CreateHomework from "../components/CreateHomework.jsx"
import {Box, Button, IconButton} from '@mui/material'
import Stepper from '@mui/material/Stepper'
import Tooltip from '@mui/material/Tooltip'
import {stepClasses} from '@mui/joy/Step'
import Step from '@mui/material/Step'
import StepIndicator, {stepIndicatorClasses} from '@mui/joy/StepIndicator'
import ShoppingCartRoundedIcon from '@mui/icons-material/ShoppingCartRounded'
import AssignmentRoundedIcon from '@mui/icons-material/AssignmentRounded'
import CheckCircleRoundedIcon from '@mui/icons-material/CheckCircleRounded'
import ArrowBackRoundedIcon from '@mui/icons-material/ArrowBackRounded'
import ArrowForwardRoundedIcon from '@mui/icons-material/ArrowForwardRounded'
import RubricComponent from "../components/RubricComponent.jsx"
import HomeworkConfirmation from '../components/HomeworkConfirmation.jsx'
import {Link} from "react-router-dom"
//import { sendEmail } from '../app/api/emails/envioCodigoDeTarea.jsx'
import CodigoDeTarea from "../app/emails/CodigoDeTarea.jsx"
import {render} from '@react-email/components'


//Aqui se supone que se creará la tarea, para esto llamará a los componentes necesarios
export const Tarea = () => {

    const [creationIndex, setCreationIndex] = React.useState(0)
    const [rubricParameters, setParametrosRubrica] = React.useState([])
    const [errorEnRubrica, setErrorEnRubrica] = React.useState(false)
    const [homeworkParameters, setHomeworkParameters] = React.useState({
        taskName: '',
        description: '',
        studentList: ''
    })
    //Estas funciones recibe la informacion que da el componente
    const setTaskData = (data) => {
        console.log("Datos recibidos desde CrearTareas:", data)


    }
    const setTaskDataRubrica = (data) => {
        console.log("Datos recibidos desde rubrica:", data)
        console.log("TaskName", data[0].taskName)
        setParametrosRubrica(data)

    }

    //Cambia el indice por lo que se cambia entre, creartarea, rubrica y finalizar(Confirmar)
    const cambiarIndice = async (numero) => {
        console.log(homeworkParameters)
        console.log("Indice", creationIndex) //esto es como para comprobar cosas despues

        if (numero === 1) {
            if (creationIndex === 1) {
                let hayErrorEnContenido = comprobarSiNoHayErrorEnLaRubrica()
                console.log(hayErrorEnContenido)
                if (!(hayErrorEnContenido || errorEnRubrica)) {
                    setCreationIndex((prevIndice) => prevIndice + 1) // Usar la versión más reciente del estado
                }
            } else if (creationIndex === 2) {
                reiniciarParametros()
                setCreationIndex(0)
                const html = await imprimirHtml() //Se obtiene el html a mandar
                await mandarCorreos(html, obtenerArregloDeCorreos())
            } else {
                setCreationIndex((prevIndice) => prevIndice + 1) // Usar la versión más reciente del estado
            }
        } else {
            if (creationIndex !== 0) {
                setCreationIndex((prevIndice) => prevIndice - 1) // Usar la versión más reciente del estado
            }
        }
    }

    //Borra las variables, se supone que antes de estoy deberia enviarlo al backend peor pues eso todavia (15oct) no
    const reiniciarParametros = () => {

        setParametrosRubrica([])
        setHomeworkParameters({
            taskName: '',
            description: '',
            studentList: ''
        })
    }
    const mandarCorreos = async (html, to) => {
        try {
            const response = await fetch('http://127.0.0.1:5000/tarea/email/code', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({html: html, to: to})
            })

            const data = await response.json()
            console.log(data.message)
        } catch (error) {
            console.log(`Error al enviar la rúbrica: ${error.message}`)
        }
    }
    const imprimirHtml = async () => {
        try {
            return await render(<CodigoDeTarea validationCode={1234}/>)
        } catch (error) {
            return ""
        }

    }
    const obtenerArregloDeCorreos = () => {
        let stringEmails = homeworkParameters.studentList
        stringEmails = stringEmails.trim() //Quitar los espacios
        return stringEmails.split(',') //Separar los correos
    }
    const comprobarSiNoHayErrorEnLaRubrica = () => {
        let hayError = false
        setErrorEnRubrica(rubricParameters.length === 0)
        const newParameters = rubricParameters.map(param => {
            if (param.totalValue === 0) {
                hayError = true
                return {...param, error: true}
            }
            return param
        })

        const updatedParameters = newParameters.map(param => {
            const updatedCriterias = param.criterias.map(criteria => {
                hayError = !criteria.rating.trim() || !criteria.description.trim()
                return {...criteria, error: !criteria.rating.trim() || !criteria.description.trim()}
            })
            return {...param, criterias: updatedCriterias}
        })

        setParametrosRubrica(updatedParameters)
        return hayError
    }
    return (
        <Box sx={{maxWidth: '700px', margin: '0 auto', padding: '2rem', border: '1px solid #ddd', borderRadius: '8px'}}>

            {creationIndex === 0 && (
                <CreateHomework 
                    homeworkParameters={homeworkParameters} 
                    setHomeworkParameters={setHomeworkParameters}
                    />)}
            {creationIndex === 1 && (
                <RubricComponent 
                    parameters={rubricParameters} 
                    setParameters={setParametrosRubrica}
                    error={errorEnRubrica} 
                    setError={setErrorEnRubrica}
                    />)}
            {creationIndex >= 2 && (
                <HomeworkConfirmation 
                    rubricParameters={rubricParameters} 
                    homeworkParameters={homeworkParameters}
                        />)}

            <Box sx={{minHeight: '10vh'}}/>

            <Box sx={{display: 'flex', alignItems: 'left', gap: 0.5}}>

                {/* Botón izquierdo */}
                <IconButton onClick={() => {
                    cambiarIndice(0)
                }} sx={{mr: 'auto'}}>
                    <ArrowBackRoundedIcon/>
                </IconButton>

                {/* Botón derecho */}
                {creationIndex < 2 && (
                    <IconButton onClick={() => {
                        cambiarIndice(1)
                    }} sx={{ml: 'auto'}}>
                        <ArrowForwardRoundedIcon/>
                    </IconButton>)}
                {
                    creationIndex >= 2 && (
                        <Button onClick={() => {
                            cambiarIndice(1)
                        }} sx={{ml: 'auto'}} component={Link} to={creationIndex === 2 ? "/Tarea" : ""}>
                            Crear
                        </Button>)
                }
            </Box>


            <Stepper
                size="lg"
                sx={{
                    width: '100%',
                    '--StepIndicator-size': '3rem',
                    '--Step-connectorInset': '1px',
                    mb: 'auto',
                    [`& .${stepIndicatorClasses.root}`]: {
                        borderWidth: 4,
                    },
                    [`& .${stepClasses.root}::after`]: {
                        height: 4,
                    },
                    [`& .${stepClasses.completed}`]: {
                        [`& .${stepIndicatorClasses.root}`]: {
                            borderColor: 'primary.300',
                            color: 'primary.300',
                        },
                        '&::after': {
                            bgcolor: 'primary.300',
                        },
                    },
                    [`& .${stepClasses.active}`]: {
                        [`& .${stepIndicatorClasses.root}`]: {
                            borderColor: 'currentColor',
                        },
                    },
                    [`& .${stepClasses.disabled} *`]: {
                        color: 'neutral.outlinedDisabledColor',
                    },
                }}
            >
                <Tooltip title="Crear tarea">
                    <Step
                        completed={creationIndex > 0}
                        active={creationIndex === 0}
                        orientation="vertical"
                        indicator={
                            <StepIndicator variant="outlined" color="primary">
                                <ShoppingCartRoundedIcon/>
                            </StepIndicator>
                        }
                    />
                </Tooltip>
                <Tooltip title="Crear Rúbrica">
                    <Step
                        orientation="vertical"
                        completed={creationIndex > 1}
                        active={creationIndex === 1}
                        disabled={creationIndex < 1}
                        indicator={
                            <StepIndicator variant="outlined" color="primary">
                                <AssignmentRoundedIcon/>
                            </StepIndicator>
                        }
                    />
                </Tooltip>
                <Tooltip title=" Finalizar">
                    <Step
                        orientation="vertical"

                        completed={creationIndex > 2}
                        active={creationIndex === 2}
                        disabled={creationIndex < 2}
                        indicator={
                            <StepIndicator >
                                hola
                                <CheckCircleRoundedIcon/>
                            </StepIndicator>
                        }
                    />
                </Tooltip>
            </Stepper>
        </Box>
    )
}
export default Tarea


