import { Box, Typography, List, ListItem, ListItemText } from '@mui/material';
import * as React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Collapse, IconButton} from '@mui/material';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';

export const ConfirmacionDeTarea = ({ parametrosRubrica, parametrosTarea }) => {
    
  const [open, setOpen] = React.useState([]);
  const handleRowClick = (index) => {
    setOpen((prev) => ({
      ...prev,
      [index]: !prev[index], // Alternar el estado de la fila específica
    }));
  };


  //Esto es para crear el row, tambien se hace el de colapse para los criterios
  const row = (rubrica,indice)=>{
    return(
   <React.Fragment>
        <TableRow >
              <TableCell> 
                <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => handleRowClick(indice)}
          >
            {open[indice] ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
          </TableCell>
              <TableCell>{rubrica.title}</TableCell>
              <TableCell>{rubrica.description}</TableCell>
              <TableCell>{rubrica.totalValue}</TableCell>
        </TableRow>
    <TableRow>
        <TableCell>
            <Collapse in = {open[indice] && rubrica.criterias.length>indice} timeout='auto' unmountOnExit >
                <Box>
                    <Typography variant="body2"><strong>Criterios:</strong> </Typography>
                    <Table size="small" aria-label="purchases">
                        <TableHead>
                        <TableRow>
                            <TableCell>Evaluacion</TableCell>
                            <TableCell>Descripcion</TableCell>
                            <TableCell align="right">Valor Parcial </TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                   {rubrica.criterias.map((criterios,indice) =>{
                    return(
                        <TableRow key = {criterios.rating}>
                            <TableCell>{criterios.rating}</TableCell>
                            <TableCell>{criterios.description}</TableCell>
                            <TableCell>{criterios.partialValue}</TableCell>
                        </TableRow>
                    )

                   })} 
                </TableBody>
                    </Table>
                </Box>
            </Collapse>
        </TableCell>
    </TableRow>
   </React.Fragment> 

    )}
  return (
    <Box>
      {/* Mostrar datos de parametrosTarea */}
      <Typography variant="h6" gutterBottom>
        Detalles de la Tarea
      </Typography>
      <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Nombre de la tarea</TableCell>
            <TableCell>Descripcion</TableCell>
            <TableCell>Lista de alumnos</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        <TableRow>
            <TableCell>{parametrosTarea.taskName}</TableCell>
            <TableCell>{parametrosTarea.description}</TableCell>
            <TableCell>{parametrosTarea.studentList}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </TableContainer>

      {/* Mostrar datos de parametrosRubrica */}
      <Typography variant="h6" gutterBottom sx={{ marginTop: 2 }}>
        Detalles de la Rúbrica
      </Typography>
      {/*Tabla de la rubrica */}
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Criterios</TableCell>
            <TableCell>Titulo</TableCell>
            <TableCell>Descripcion</TableCell>
            <TableCell>Valor</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {parametrosRubrica.map((rubrica, indice) => (
            row(rubrica,indice)
          ))}
        </TableBody>
      </Table>
    </TableContainer>

  </Box>
  );
};

export default ConfirmacionDeTarea;
