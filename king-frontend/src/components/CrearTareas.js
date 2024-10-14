import React, { useState } from 'react';
import { Box, TextField, Typography, Stack } from '@mui/material';

export const CrearTarea = () => {
  const [nombreTarea, setNombreTarea] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [listaNombres, setListaNombres] = useState('');

  const handleEnvio = (e) => {
    e.preventDefault();
    console.log("Nombre de la Tarea:", nombreTarea);
    console.log("Descripción:", descripcion);
    console.log("Lista de Nombres:", listaNombres);
    // Aquí puedes manejar el envío de datos
  };

  return (
    <Box >
      <Typography variant="h5" component="h1" gutterBottom>
        Crear Tarea
      </Typography>
      <form onSubmit={handleEnvio}>
        <Stack spacing={3}>
          <TextField
            label="Nombre de la Tarea"
            variant="outlined"
            fullWidth
            value={nombreTarea}
            onChange={(e) => setNombreTarea(e.target.value)}
          />
          <TextField
            label="Descripción"
            variant="outlined"
            fullWidth
            multiline
            rows={4}
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
          />
          <TextField
            label="Lista de Nombres"
            variant="outlined"
            fullWidth
            value={listaNombres}
            onChange={(e) => setListaNombres(e.target.value)}
            placeholder="Separar nombres por comas"
          />
          </Stack>
      </form>
      
    </Box>
  );
};
export default CrearTarea 
