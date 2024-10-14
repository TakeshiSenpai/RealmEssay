import React, { PureComponent } from 'react'
import CrearTareas from "../components/CrearTareas.js"
import { Box, Button} from '@mui/material';
import Stepper from '@mui/joy/Stepper';
import Tooltip from '@mui/joy/Tooltip';
import Step, { stepClasses } from '@mui/joy/Step';
import StepIndicator, { stepIndicatorClasses } from '@mui/joy/StepIndicator';
import ShoppingCartRoundedIcon from '@mui/icons-material/ShoppingCartRounded';
import ContactsRoundedIcon from '@mui/icons-material/ContactsRounded';
import LocalShippingRoundedIcon from '@mui/icons-material/LocalShippingRounded';
import AssignmentRoundedIcon from '@mui/icons-material/AssignmentRounded';
import CheckCircleRoundedIcon from '@mui/icons-material/CheckCircleRounded';

export const Tarea = ()=>{
    const handleData = (data) => {
        console.log("Datos recibidos desde CrearTareas:", data);
        // Aquí puedes manejar los datos como necesites
      };

    return(
        <Box sx={{ maxWidth: '700px', margin: '0 auto', padding: '2rem', border: '1px solid #ddd', borderRadius: '8px' }}>
    
        <CrearTareas onSendData={handleData}/>

        <Box sx ={{minHeight: '10vh'}}/>

        
    

        <Stepper
      size="lg"
      sx={{
        width: '100%',
        '--StepIndicator-size': '3rem',
        '--Step-connectorInset': '0px',
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
        completed
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
        completed
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
        active
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


