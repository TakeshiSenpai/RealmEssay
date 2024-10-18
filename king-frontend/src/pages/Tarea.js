import React, { PureComponent } from 'react'
import CrearTareas from "../components/CrearTareas.js"
import { Box, Button, IconButton} from '@mui/material';
import Stepper from '@mui/joy/Stepper';
import Tooltip from '@mui/joy/Tooltip';
import Step, { stepClasses } from '@mui/joy/Step';
import StepIndicator, { stepIndicatorClasses } from '@mui/joy/StepIndicator';
import ShoppingCartRoundedIcon from '@mui/icons-material/ShoppingCartRounded';
import AssignmentRoundedIcon from '@mui/icons-material/AssignmentRounded';
import CheckCircleRoundedIcon from '@mui/icons-material/CheckCircleRounded';
import ArrowBackRoundedIcon from '@mui/icons-material/ArrowBackRounded';
import ArrowForwardRoundedIcon from '@mui/icons-material/ArrowForwardRounded';
import { FlashOnRounded } from '@mui/icons-material';
import ComponenteRubrica from "../components/ComponenteRubrica.js"
import ConfirmacionDeTarea from '../components/ConfirmacionDeTarea.js';
import { Link } from "react-router-dom";
//import { sendEmail } from '../app/api/emails/envioCodigoDeTarea.jsx';
import CodigoDeTarea from "../app/emails/CodigoDeTarea.jsx"
import { render } from '@react-email/components';


//Aqui se supone que se creará la tarea, para esto llamará a los componentes necesarios
export const Tarea = ()=>{

  const [indiceDeCreacion,setIndiceDeCreacion] = React.useState(0)
  const [parametrosRubrica, setParametrosRubrica] = React.useState([])
  const [errorEnRubrica, setErrorEnRubrica] = React.useState(false)
  const [parametrosTarea,setParametrosTarea] = React.useState({
    taskName:'',
    description:'',
    studentList:''
  })
  //Esta funcion recibe la informacion que da el componente
    const setTaskData = (data) => {
        console.log("Datos recibidos desde CrearTareas:", data)
        
        
      };
    const setTaskDataRubrica = (data) => {
      console.log("Datos recibidos desde rubrica:", data)
      console.log("TaskName",data[0].taskName)
      setParametrosRubrica(data)
      
    };
  
    //Cambia el indice por lo que se cambia entre, creartarea, rubrica y finalizar(Confirmar)
    const cambiarIndice = async (numero) => {
      console.log(parametrosTarea);
      console.log("Indice", indiceDeCreacion); //esto es como para comprobar cosas despues 
      
      if (numero === 1) {
        if (indiceDeCreacion === 1) {
          let hayErrorEnContenido = comprobarSiNoHayErrorEnLaRubrica();
          if (!(hayErrorEnContenido || errorEnRubrica)) {
            setIndiceDeCreacion((prevIndice) => prevIndice + 1); // Usar la versión más reciente del estado
          }
        } else if (indiceDeCreacion === 2) {
          reiniciarParametros();
          setIndiceDeCreacion(0);
          const html = await imprimirHtml(); //Se obtiene el html a mandar 
          await mandarCorreos(html, obtenerArregloDeCorreos());
        } else {
          setIndiceDeCreacion((prevIndice) => prevIndice + 1); // Usar la versión más reciente del estado
        }
      } else {
        if (indiceDeCreacion !== 0) {
          setIndiceDeCreacion((prevIndice) => prevIndice - 1); // Usar la versión más reciente del estado
        }
      }
    };
    
      //Borra las variables, se supone que antes de estoy deberia enviarlo al backend peor pues eso todavia (15oct) no 
      const reiniciarParametros = ()=>{
        
        setParametrosRubrica([])
        setParametrosTarea({
          taskName:'',
          description:'',
          studentList:''
        })
      }
      const mandarCorreos= async (html,to)=>{
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
      const imprimirHtml = async ()=>{
        try{
        const html = await render(<CodigoDeTarea validationCode={1234}/>)
        return html
      }
        catch(error){
          return ""
        }

      }
      const obtenerArregloDeCorreos = ()=>{
        let stringEmails = parametrosTarea.studentList
        stringEmails = stringEmails.trim() //Quitar los espacios
        return stringEmails.split(',') //Separar los correos
      }
      const comprobarSiNoHayErrorEnLaRubrica = ()=>{
        let hayError = false
        setErrorEnRubrica(parametrosRubrica.length ===0)
        const newParameters = parametrosRubrica.map(param => {
          if (param.totalValue === 0) {
              hayError = true
              return {...param, error: true}
          }
          return param
      })

      const updatedParameters = newParameters.map(param => {
          const updatedCriterias = param.criterias.map(criteria => {
            hayError = true
              return {...criteria, error: !criteria.rating.trim() || !criteria.description.trim()}
          })
          return {...param, criterias: updatedCriterias}
      })

      setParametrosRubrica(updatedParameters)
      return hayError
      }
    return(
        <Box sx={{  maxWidth: '700px', margin: '0 auto', padding: '2rem', border: '1px solid #ddd', borderRadius: '8px' }}>
    
          {indiceDeCreacion=== 0 &&(<CrearTareas parametrosTarea={parametrosTarea} setParametrosTarea={setParametrosTarea}/>)}
          {indiceDeCreacion=== 1 &&(<ComponenteRubrica parameters={parametrosRubrica} setParameters={setParametrosRubrica} error={errorEnRubrica}/>)}
          {indiceDeCreacion >= 2 && (<ConfirmacionDeTarea parametrosRubrica={ parametrosRubrica} parametrosTarea={parametrosTarea}/>)}

        <Box sx ={{minHeight: '10vh'}}/>

        <Box sx={{display: 'flex', alignItems:'left',gap: 0.5}}>

          {/* Botón izquierdo */}          
          <IconButton onClick={()=>{cambiarIndice(0) }}  sx={{mr:'auto'}}>
          <ArrowBackRoundedIcon/>
          </IconButton>

          {/* Botón derecho */}
          { indiceDeCreacion <2 &&(
          <IconButton onClick={()=>{cambiarIndice(1) }} sx={{ml:'auto'}}   >
          <ArrowForwardRoundedIcon/>
          </IconButton>)}
          {
              indiceDeCreacion >=2 &&(
              <Button onClick={()=>{cambiarIndice(1) }} sx={{ml:'auto'}} component={Link} to = { indiceDeCreacion===2 ? "/Tarea" : ""}>
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
        mb:'auto',
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
      <Tooltip title= "Crear tarea">
      <Step
        completed={ indiceDeCreacion>0 ? true :false}
        active = {indiceDeCreacion ===0 ? true :false}
        orientation="vertical"
        indicator={
          <StepIndicator variant="outlined" color="primary">
            <ShoppingCartRoundedIcon />
          </StepIndicator>
        }
      />
      </Tooltip>
      <Tooltip title= "Crear Rúbrica">
      <Step
        orientation="vertical"
        completed={ indiceDeCreacion>1 ? true :false}
        active = {indiceDeCreacion ===1 ? true :false}
        disabled = {indiceDeCreacion < 1? true: false}
        indicator={
          <StepIndicator variant="outlined" color="primary">
            <AssignmentRoundedIcon />
          </StepIndicator>
        }
      />
      </Tooltip>
      <Tooltip title= " Finalizar">
      <Step
        orientation="vertical"
        
        completed={ indiceDeCreacion>2 ? true :false}
        active = {indiceDeCreacion ===2 ? true :false}
        disabled = {indiceDeCreacion < 2? true: false}
        indicator={
          <StepIndicator variant="outlined" color="primary">
            <CheckCircleRoundedIcon />
          </StepIndicator>
        }
      />
    </Tooltip>
    </Stepper>
        </Box>
    )
}
export default Tarea;


