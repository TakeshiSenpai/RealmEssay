import Button from '@mui/joy/Button';
import Drawer from '@mui/joy/Drawer';
import React, { useEffect, useState } from 'react';
import List from '@mui/joy/List';
import ListItem from '@mui/joy/ListItem';
import ListItemDecorator from '@mui/joy/ListItemDecorator';
import IconButton from '@mui/joy/IconButton';
import Avatar from '@mui/joy/Avatar';
import DialogTitle from '@mui/joy/DialogTitle';
import DialogContent from '@mui/joy/DialogContent';
import Box from '@mui/joy/Box';
import Typography from '@mui/joy/Typography';
import { Outlet, Link } from "react-router-dom";
import { ChangeCircleTwoTone, ExitToApp, Home, MenuBookOutlined } from '@mui/icons-material';
import { ListItemButton, ListItemContent } from '@mui/joy';
import { useNavigate } from 'react-router-dom'; 

const Layout = () => {
  const [open, setOpen] = React.useState(false);
  const setMenuOpen = React.useState(null);  
  const [userInfo, setUserInfo] = useState({ name: '', institution: '', picture: '' });
  const navigate = useNavigate(); 
  
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
  
  return (
    <React.Fragment>
      <IconButton variant="outlined" color="neutral" onClick={() => setOpen(true)}>
        <MenuBookOutlined />
      </IconButton>
      <Drawer open={open} onClose={() => setOpen(false)}>
        <DialogTitle>
          Envio de ensayos
        </DialogTitle>
        <DialogContent>
          <List>
            <ListItem>
              <ListItemButton component={Link} to="/" onClick={() => setOpen(false)}> 
                <ListItemDecorator><Home /></ListItemDecorator> 
                <ListItemContent>Home</ListItemContent>
              </ListItemButton>
            </ListItem>
            <ListItem>
              <ListItemButton component={Link} to="/blogs" onClick={() => setOpen(false)}> 
                <ListItemDecorator>🧅</ListItemDecorator> 
                <ListItemContent>Blogs</ListItemContent>
              </ListItemButton>
            </ListItem>
          </List>
        </DialogContent>
        <Box
          sx={{
            display: 'flex',
            gap: 1,
            p: 1.5,
            pb: 2,
            borderTop: '3px solid',
            borderColor: 'divider',
          }}
        >
          {/* Muestra la foto del usuario si está disponible */}
          <Avatar size="lg" src={userInfo.picture} alt={userInfo.name} />
          <div>
            {/* Mostrar la información almacenada en localStorage */}
            <Typography level="title-md">{userInfo.name}</Typography>
            <Typography level="body-sm">{userInfo.institution}</Typography>
          </div>      

          {/* Botón de cerrar sesión */}
          <Button variant="outlined" color="neutral" size="md" onClick={() => {
            localStorage.clear(); 
            navigate('/auth'); 
          }}>
            <ExitToApp />
          </Button>

          <Button variant="outlined" color="neutral" size="md" >
            <ChangeCircleTwoTone />
          </Button>
        </Box>
      </Drawer>
      <Outlet />
    </React.Fragment>
  );
};

export default Layout;
