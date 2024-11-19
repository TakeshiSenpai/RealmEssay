import React, {useEffect} from 'react'
import CreateHomework from "../components/Homeworks/CreateHomework.jsx"
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
import RubricComponent from "../components/Homeworks/RubricComponent.jsx"
import HomeworkConfirmation from '../components/Homeworks/HomeworkConfirmation.jsx'
import {Link, useNavigate} from "react-router-dom"
//import { sendEmail } from '../app/api/emails/envioCodigoDeTarea.jsx'
import CodigoDeTarea from "../app/emails/CodigoDeTarea.jsx"
import {render} from '@react-email/components'
import EmailProfesorConfirmation from '../app/emails/EmailProfesorConfirmation.jsx'
import {useIsStudent} from "../components/IsStudentProvider"


//Aqui se supone que se creará la tarea, para esto llamará a los componentes necesarios
const Homework = () => {

    const [creationIndex, setCreationIndex] = React.useState(0)
    const [idHomework,setIDHomework] = React.useState()
    const [textRubric,setTextRubric] = React.useState()
    const [rubricParameters, setParametrosRubrica] = React.useState([])
    const [errorEnRubrica, setErrorEnRubrica] = React.useState(true)
    const [homeworkParameters, setHomeworkParameters] = React.useState({
        taskName: '',
        description: '',
        studentList: ''
    })

    const {isStudent, setIsStudent} = useIsStudent()
    const navigate = useNavigate()
    useEffect(() => {
        console.log(isStudent);
        if (!isStudent) {
            navigate("/")
            setIsStudent(true)
        }
    }, [])

    //Estas funciones recibe la informacion que da el componente

    const IAUrl = process.env.REACT_APP_VERCEL_IA
                ? `https://${process.env.REACT_APP_VERCEL_IA}`
                : 'http://127.0.0.1:2003'

    const teacherURL = process.env.REACT_APP_VERCEL_HOMEWORK_TEACHER
                ? `https://${process.env.REACT_APP_VERCEL_HOMEWORK_TEACHER}`
                : 'http://127.0.0.1:2002'
    //Cuando se use esto es porque el profesor creo la tarea, se puede decir que este es el ulitmo paso
    //Aqui se guarda la informacion en la base de datos
    useEffect( ()=>{
        async function envairCoreoConfirmacion(){
        console.log("Estamos en el useEffect",textRubric);
        if(textRubric !== undefined){
            const storedUserInfo = localStorage.getItem('userInfo')
            const parsedUserInfo = JSON.parse(storedUserInfo)
            const homeworkParametersCopy = homeworkParameters
            reiniciarParametros();
            const html = await printHtmlConfirmation(homeworkParametersCopy,parsedUserInfo.name)
            const payload = {
                email: parsedUserInfo.email,
                name: parsedUserInfo.name,
                homeworkParameters: homeworkParametersCopy,
                htmlContent: html,
            }
            console.log(payload)
            await updateBD(homeworkParametersCopy,parsedUserInfo.email)

            const to = []
            to.push(parsedUserInfo.email)
            //Comentado porque no quiero mil correos de momento
           await mandarCorreos(html,to, "Confirmación de tarea")
        }
    
    }
    envairCoreoConfirmacion()
    },[textRubric])
 
    //Cambia el indice por lo que se cambia entre, creartarea, rubrica y finalizar(Confirmar)
    const cambiarIndice = async (numero) => {
        console.log(homeworkParameters)
        console.log("Indice", creationIndex) //esto es como para comprobar cosas despues
        
        if (numero === 1) {
            if (creationIndex === 1) {
                console.log ("Si es uno")
                let hayErrorEnContenido =  comprobarSiNoHayErrorEnLaRubrica()
                console.log(hayErrorEnContenido)
                if (!(hayErrorEnContenido || errorEnRubrica)) {
                    setCreationIndex((prevIndice) => prevIndice + 1) // Usar la versión más reciente del estado
                }
            } else if (creationIndex === 2) {
                //Si entra aqui quiere decir que le dió en crear
                setCreationIndex(0)
                const htmlCode = await printHtmlValidationCode() //Se obtiene el html a mandar
                await mandarCorreos(htmlCode, obtenerArregloDeCorreos(), "Código de enivío de ensayo")
                //Ahora se manda el correo de confirmacion
                await getTextRubric() 
            } else {
                setCreationIndex((prevIndice) => prevIndice + 1) // Usar la versión más reciente del estado
            }
        } else {
            if (creationIndex !== 0) {
                setCreationIndex((prevIndice) => prevIndice - 1) // Usar la versión más reciente del estado
            }
        }
    }
    //Aqui basicamente se hará un post a la base de datos de tarea
    const updateBD = async (homeworkParametersCopy,profesor)=>{
        try {
            const response = await fetch(`${teacherURL}/tarea/postDB`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id:idHomework,
                    Nombre: homeworkParametersCopy.taskName,
                    Profesor: profesor,
                    Descripcion: homeworkParametersCopy.description,
                    Rubrica: textRubric,
                    Alumnos:obtenerArregloDeCorreos() 
                })
            })

            const data = await response.json()
            console.log(data.message)
        } catch (error) {
            console.log(`Error al guardar la tarea: ${error.message}`)
        }
    }
    const getTextRubric= async ()=>{
        try {
            const response = await fetch(`${IAUrl}/tarea/rubrica`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({rubrica: rubricParameters})
            })

            const data = await response.json()
            console.log(data.message)
            setTextRubric(data.message)
        } catch (error) {
            console.log(`Error al enviar la rúbrica: ${error.message}`)
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
    const mandarCorreos = async (html, to, subject) => {
        try {
            const response = await fetch(`${teacherURL}/tarea/email/code`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({html: html, to: to, subject: subject})
            })

            const data = await response.json()
            console.log(data.message, "A ", to.length)
        } catch (error) {
            console.log(`Error al enviar la rúbrica: ${error.message}`)
        }
    }
    const printHtmlValidationCode = async () => {
        try {
            //Numero random de entre 11111 a 99999
            //Deberia haber una comprobacion en la base de datos antes
            //const randomNumber = obtenerID() //Aqui se obtiene el numero random pero tomando en cuenta la bd
            var randomNumber =Math.floor(Math.random() * (99999 - 11111 + 1)+ 11111)
            setIDHomework(randomNumber)
            return await render(<CodigoDeTarea validationCode={randomNumber}/>)
        } catch (error) {
            return ""
        }

    }
    const printHtmlConfirmation = async (homeworkParametersCopy,profesor) =>{
        try{

            let textHomework = "Nombre de tarea" + homeworkParametersCopy.taskName
            + "Descripción: " + homeworkParametersCopy.description + "Estudiantes registrados " + homeworkParametersCopy.studentList;

            return await render (<EmailProfesorConfirmation 
                textHomework = {textHomework} 
                textRubric={textRubric}
                profesor={profesor}
                />)
        }
        catch{
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
        console.log("Valor Error Rubrica",errorEnRubrica)
        const newParameters = rubricParameters.map(param => {
            if (param.totalValue === 0) {
                console.log("Entro al map")
                hayError = true
                return {...param, error: true}
            }
            return param
        })
        console.log("Valor de hayError",hayError)
        const updatedParameters = newParameters.map(param => {
            const updatedCriterias = param.criterias.map(criteria => {
                console.log("Entro al map")
                hayError = !criteria.rating.trim() || !criteria.description.trim()
                return {...criteria, error: !criteria.rating.trim() || !criteria.description.trim()}
            })
            return {...param, criterias: updatedCriterias}
        })

        setParametrosRubrica(updatedParameters)
        return hayError
    }
    return (
        <Box sx={{paddingY: 4}}>
        <Box sx={{maxWidth: '700px', margin: '0 auto', padding: '2rem', border: '1px solid #ddd', borderRadius: '29px'}}>

            {creationIndex === 0 && (
                <CreateHomework 
                    homeworkParameters={homeworkParameters} 
                    setHomeworkParameters={setHomeworkParameters}
                    />)}
            {(creationIndex === 1 ) && (
                <RubricComponent 
                    parameters={rubricParameters} 
                    setParameters={setParametrosRubrica}
                    error={errorEnRubrica} 
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
                        }} 
                        sx={{ml: 'auto'}} 
                        >
                            Crear
                        </Button>)
                        //component={Link} to={creationIndex === 2 ? "essays/createhomework" : ""}
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
        </Box>
    )
}
export default Homework


