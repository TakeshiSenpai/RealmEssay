import Button from '@mui/joy/Button';
import Drawer from '@mui/material/Drawer';
import React, { useEffect, useState } from 'react';
import List from '@mui/joy/List';
import ListItem from '@mui/joy/ListItem';
import IconButton from '@mui/material/IconButton';
import Avatar from '@mui/joy/Avatar';
import DialogTitle from '@mui/joy/DialogTitle';
import DialogContent from '@mui/joy/DialogContent';
import Box from '@mui/joy/Box';
import Typography from '@mui/joy/Typography';
import ViewSidebarRoundedIcon from '@mui/icons-material/ViewSidebarRounded';
import { Outlet, Link } from "react-router-dom";
import {ListItemButton, ListItemContent, ListItemDecorator} from '@mui/joy';
import { useNavigate } from 'react-router-dom'; 
import Tooltip from '@mui/joy/Tooltip';
import {Divider } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import FormControl from '@mui/joy/FormControl';
import Input from '@mui/joy/Input';
import Modal from '@mui/joy/Modal';
import ModalDialog from '@mui/joy/ModalDialog';
import Stack from '@mui/joy/Stack';
import LightModeRoundedIcon from '@mui/icons-material/LightModeRounded';
import Switch from '@mui/joy/Switch';
import Dropdown from '@mui/joy/Dropdown';
import Menu from '@mui/joy/Menu';
import MenuButton from '@mui/joy/MenuButton';
import MenuItem from '@mui/joy/MenuItem';
import MoreVert from '@mui/icons-material/MoreVert';
import DarkModeRoundedIcon from '@mui/icons-material/DarkModeRounded';
import {BluetoothAudio, EditNote} from "@mui/icons-material";

const drawerWidth = 240;  // Define el a
const Layout = () => {
  const [open, setOpen] = React.useState(false);
  const [openModal, setOpenModal] = React.useState(false);  
  const [userInfo, setUserInfo] = useState({ name: '', institution: '', picture: '' });
  const [arregloDeConversaciones,setArregloDeConversaciones] = useState(["Home"]);
  const [arregloDeTareas,setArregloDeTareas] = useState(["Primera Tarea"]);
  
  const navigate = useNavigate(); 
  const [dark, setDark] = React.useState(false);
  const [esAlumno,setAlumno] = React.useState(true);
  useEffect(() => {
    const storedUserInfo = localStorage.getItem('userInfo');
    
    if (storedUserInfo) {
      const parsedUserInfo = JSON.parse(storedUserInfo);

      console.log(parsedUserInfo)
      
      setUserInfo({
        name: parsedUserInfo.name,
        institution: parsedUserInfo.institution,
        picture: parsedUserInfo.picture 
      });
    }
  }, []);
  
  const addArregloDeConversaciones = (codigo)=>{
    setArregloDeConversaciones([...arregloDeConversaciones,codigo])

  }
  const cambiarVista = ()=>{
    setAlumno(!esAlumno);
  }
  const addArregloDeTareas = (nombre)=>{
    setArregloDeConversaciones([...arregloDeConversaciones,nombre])

  }


  const mostrarContenidoEnSidebarListItem=()=>{
    if(esAlumno){
      return [
        arregloDeConversaciones.map((_, index) => (
          <ListItem key={index}>
            <ListItemButton component={Link} to="/" >
              {arregloDeConversaciones[index].length > 30?arregloDeConversaciones[index].slice(0,25)+"...":arregloDeConversaciones[index]  }
            </ListItemButton>
          </ListItem>
        ))
      ]
    }
    return [
      arregloDeTareas.map((_, index) => (
        <ListItem key={index}>
          <ListItemButton component={Link} to="/" >
            {arregloDeTareas[index].length > 30?arregloDeTareas[index].slice(0,25)+"...":arregloDeTareas[index]  }
          </ListItemButton>
        </ListItem>
      ))
    ]

  }
  return (
    <Box sx={{ display: 'flex' }}>
      
      <Drawer open={open}  onClose={() => setOpen(false)  } sx={{
          width: 240,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: 240,
            boxSizing: 'border-box',
          },
        }}
        variant="persistent"
        anchor="left"
        >
          <Box sx={{
      borderRadius: '8px',
      padding: '6px',
      display: 'flex', // Asegúrate de que el contenedor sea flex
      justifyContent: 'space-between', // Espacio entre los botones
    }} >
          <Tooltip title= "Cerrar menú"> 
            <IconButton sx={{mr:'auto'}} color="neutral" aria-label="delete" onClick={() => setOpen(false)}>
            <ViewSidebarRoundedIcon/>
            </IconButton>
          </Tooltip>
          <Tooltip title= {esAlumno ? "Ingresar codigo de conversacion" : "Crear Tarea"}> 
            <IconButton sx={{ml:'auto'}}color="neutral" aria-label="delete" component={Link} to={esAlumno ? "/" : "/Tarea"} onClick={esAlumno
            ?() => setOpenModal(true) : () => setOpen(true)}>
            <AddIcon/>
            </IconButton>

          </Tooltip>
          <Modal open={openModal} onClose={() => setOpenModal(false)}>
        <ModalDialog>
          <DialogTitle>Ingresa el código de chat</DialogTitle>
          <DialogContent>El código debe ser proporcionado por su profesor</DialogContent>
          <form
            onSubmit={(event) => {
              event.preventDefault();
              setOpenModal(false);
              const formData = new FormData(event.currentTarget);
              const formJson = Object.fromEntries(formData.entries());
              addArregloDeConversaciones(formJson.codigo)
              console.log(arregloDeConversaciones)
            }}
          >
            <Stack spacing={2}>
              <FormControl>
                <Input autoFocus required name="codigo" />
              </FormControl>
              <Button type="submit">Enviar</Button>
            </Stack>
          </form>
        </ModalDialog>
      </Modal>
          </Box>
        <Divider/>
          <List>
          {
            mostrarContenidoEnSidebarListItem()
            
            }
            <ListItem>
              <ListItemButton component={Link} to="/Rubrica" >
                <ListItemDecorator>  <EditNote/>  </ListItemDecorator>
                <ListItemContent>Rúbrica</ListItemContent>
              </ListItemButton>
            </ListItem>
          </List>
        
        <Box
          sx={{
            display: 'flex',
            gap: 1,
            p: 1.5,
            pb: 4,
            borderTop: '3px solid',
            borderColor: 'divider',
          }}
        >
          {/* Muestra la foto del usuario si está disponible */}
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Avatar size="md" src={userInfo.picture} alt={userInfo.name} />
            {/* Mostrar la información almacenada en localStorage */}
            <Typography level="body-sm">{userInfo.name.length > 20?userInfo.name.slice(0,16)+"...":userInfo.name }</Typography>
            </Box>
          {/* Botón de cerrar sesión */}

          <Dropdown>
      <MenuButton
        slots={{ root: IconButton }}
        slotProps={{ root: { variant: 'outlined', color: 'neutral' } }}
        sx={{ml:'auto'}}
      >
        <MoreVert />
      </MenuButton>
      <Menu sx={{ zIndex: 1300 }}>
        <MenuItem onClick={()=>{ 
          localStorage.clear(); 
            navigate('/auth'); }}>Cerrar sesión</MenuItem>
        <MenuItem component={Link} to={!esAlumno ? "/" : "/Tarea"} onClick={()=>{ cambiarVista() }}>{esAlumno ? "Cambiar a profesor" : "Cambiar a alumno"}</MenuItem>
      </Menu>
    </Dropdown>
        
        </Box>
      </Drawer>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          padding: 3,
          transition: 'margin 0.3s ease',
          marginLeft: open ? `0px` : '-250px', // Ajusta el contenido cuando el Drawer está abierto o cerrado
        }}
      >
    {!open && (
      
      <Tooltip title = "Abrir menú">
        <IconButton sx={{
    position: 'absolute',
    top: 6, // ajusta el valor para más o menos separación
    left: 6,
  }}color="neutral" onClick={() => setOpen(true)}>
        <ViewSidebarRoundedIcon/>
        </IconButton>
        </Tooltip>
      )}
      
      <Switch size ='lg' sx={{
        position: 'absolute',
        top: 15, // ajusta el valor para más o menos separación
        right: 30,
        '& .MuiSwitch-thumb': {
          backgroundColor: dark ? 'primary.main' : 'warning.main',
        }
      }}
      checked={dark}
      onChange={(event) => setDark(event.target.checked)}
      startDecorator={dark ? <DarkModeRoundedIcon /> : <LightModeRoundedIcon />}
     />
        
      
        <Outlet />
      </Box>
    </Box>
  );
};

export default Layout;
