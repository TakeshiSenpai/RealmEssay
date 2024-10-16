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



//Aqui se supone que se creará la tarea, para esto llamará a los componentes necesarios
export const Tarea = ()=>{

  const [indiceDeCreacion,setIndiceDeCreacion] = React.useState(0)
  const [parametrosRubrica, setParametrosRubrica] = React.useState([])
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
      const cambiarIndice = (numero)=>{
        console.log(parametrosTarea)
        console.log("Indice",indiceDeCreacion) //esto es como para comprobar cosas despues 
        if (numero ===1){
          if (indiceDeCreacion!==2) setIndiceDeCreacion(indiceDeCreacion+1); 
          else {
            reiniciarParametros()
            indiceDeCreacion = 0;
            //sendEmail("hola@yopmail.com",12345)

            //Ademas de hacer esto se deberia hacer un link para la tarea o algo asi, talvez un link para el home 
          };
        }
        else{
          if (indiceDeCreacion!==0) setIndiceDeCreacion(indiceDeCreacion -1) 
        }
      }
      //Borra las variables, se supone que antes de estoy deberia enviarlo al backend peor pues eso todavia (15oct) no 
      const reiniciarParametros = ()=>{
        
        setParametrosRubrica([])
        setParametrosTarea({
          taskName:'',
          description:'',
          studentList:''
        })
      }

    return(
        <Box sx={{  maxWidth: '700px', margin: '0 auto', padding: '2rem', border: '1px solid #ddd', borderRadius: '8px' }}>
    
          {indiceDeCreacion=== 0 &&(<CrearTareas parametrosTarea={parametrosTarea} setParametrosTarea={setParametrosTarea}/>)}
          {indiceDeCreacion=== 1 &&(<ComponenteRubrica parameters={parametrosRubrica} setParameters={setParametrosRubrica}/>)}
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


