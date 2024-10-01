
import Button from '@mui/joy/Button';
import Drawer from '@mui/joy/Drawer';
import React from 'react';
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
import { ArrowDownward, ChangeCircleTwoTone, ExitToApp, Home, MenuBookOutlined } from '@mui/icons-material';
import { ListItemText } from '@mui/material';
import { Dropdown, ListItemButton, ListItemContent } from '@mui/joy';
import Menu from '@mui/joy/Menu';
import MenuButton from '@mui/joy/MenuButton';
import MenuItem from '@mui/joy/MenuItem';
import zIndex from '@mui/material/styles/zIndex';


const Layout = () => {
    const [open, setOpen] = React.useState(false);
    const [menuOpen, setMenuOpen] = React.useState(null);  
    
  const handleMenuOpen = (event) => {
    setMenuOpen(event.currentTarget);  // Abrir el menú
  };

  const handleMenuClose = () => {
    setMenuOpen(null);  // Cerrar el menú
  };



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
            <ListItemButton component ={Link} to="/" onClick={() => setOpen(false)}> 
            <ListItemDecorator><Home/></ListItemDecorator> 
            <ListItemContent>Home</ListItemContent>
            </ListItemButton>
          </ListItem>
            
          <ListItem>
            <ListItemButton component ={Link} to="/blogs" onClick={() => setOpen(false)}> 
            <ListItemDecorator>🧅</ListItemDecorator> 
            <ListItemContent>Home</ListItemContent>
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
          <Avatar size="lg" />
          <div>
            <Typography level="title-md">Username</Typography>
            <Typography level="body-sm">UABC</Typography>
          </div>      
        
      <Button variant="outlined" color="neutral" size= "md" >
        <ExitToApp/>
      </Button>
      <Button variant="outlined" color="neutral" size= "md" >
        <ChangeCircleTwoTone/>
      </Button>
        </Box>
    </Drawer>
    <Outlet />
    </React.Fragment>
  )
};

export default Layout;