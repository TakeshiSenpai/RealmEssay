import {Divider, ListItemButton} from '@mui/material'
import Drawer from '@mui/material/Drawer'
import React, {useEffect, useRef, useState} from 'react'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import IconButton from '@mui/material/IconButton'
import Avatar from '@mui/material/Avatar'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import ViewSidebarRoundedIcon from '@mui/icons-material/ViewSidebarRounded'
import {Link, Outlet, useNavigate} from "react-router-dom"
import Tooltip from '@mui/material/Tooltip'
import AddIcon from '@mui/icons-material/Add'
import LightModeRoundedIcon from '@mui/icons-material/LightModeRounded'
import Menu from '@mui/material/Menu'
import MenuItem from '@mui/material/MenuItem'
import MoreVert from '@mui/icons-material/MoreVert'
import DarkModeRoundedIcon from '@mui/icons-material/DarkModeRounded'
import {AutoAwesomeRounded, Home, PaletteRounded} from "@mui/icons-material"
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded"
import HomeworkCode from "../components/Homeworks/HomeworkCode"
import {useIsStudent} from "../components/IsStudentProvider"

// Layout es un componente que representa la estructura de la página
const Layout = ({theme, setTheme, isAuto}) => {
    const [open, setOpen] = useState(true)
    const [openModal, setOpenModal] = useState(false)
    const [userInfo, setUserInfo] = useState({name: '', institution: '', picture: ''})
    const [conversationArray, setConversationArray] = useState([])
    const [arregloDeTareas, setArregloDeTareas] = useState(["Primera Tarea"])
    const {isStudent} = useIsStudent()
    const [selectedIndex, setSelectedIndex] = useState(null);

    const navigate = useNavigate()

    const [menuOpen, setMenuOpen] = useState(false)
    const [themeMenuOpen, setThemeMenuOpen] = useState(false)
    const menuRef = useRef(null)
    useClickOutside(menuRef, () => {
        setMenuOpen(false)
        setThemeMenuOpen(false)
    })

    // Cargar la información del usuario y el tema desde localStorage
    useEffect(() => {
        const storedUserInfo = localStorage.getItem('userInfo')

        if (storedUserInfo) {
            const parsedUserInfo = JSON.parse(storedUserInfo)
            setUserInfo({
                name: parsedUserInfo.name,
                institution: parsedUserInfo.institution,
                picture: parsedUserInfo.picture,
                email: parsedUserInfo.email
            })
        }

        const savedTheme = localStorage.getItem('theme')
        if (savedTheme) setTheme(savedTheme)
        console.log(userInfo)
        if (userInfo.email) {
            addToConversationsArray(userInfo.email);
        }
    }, [userInfo.email, setTheme]);

    const addToConversationsArray = async (email) => {
        const apiGatewayURL = process.env.REACT_APP_VERCEL_API_GATEWAY
            ? `https://${process.env.REACT_APP_VERCEL_API_GATEWAY}`
            : 'http://127.0.0.1:2000'
        
        try {
            const response = await fetch(`${apiGatewayURL}/get/tareas`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email }),
            });
    
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status} ${response.statusText}`);
            }
    
            const data = await response.json();
    
            // Verifica que se haya recibido correctamente las tareas
            if (data && data.tareas) {
                const tareaNombres = data.tareas.map(tarea => tarea.Nombre +" - " +  tarea.id)
                setConversationArray(tareaNombres)
            } else {
                console.warn('No se encontraron tareas o el campo "tareas" está vacío.');
            }
        } catch (error) {
            console.error('Error al realizar la solicitud:', error);
        }
    }

    const addToConversationArray = async (code) => {
        const apiGatewayURL = process.env.REACT_APP_VERCEL_API_GATEWAY
            ? `https://${process.env.REACT_APP_VERCEL_API_GATEWAY}`
            : 'http://127.0.0.1:2000';
    
        try {
            const response = await fetch(`${apiGatewayURL}/get/tarea`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({code: code, email: userInfo.email}),
            });
    
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status} ${response.statusText}`)
            }
    
            const data = await response.json()
    
            // Verifica que data.tarea exista y tenga el campo Nombre
            if (data && data.tarea && data.tarea.Nombre) {
                setConversationArray((prevArray) => [...prevArray, (data.tarea.Nombre +" - " + data.tarea.id)])
            } else {
                console.warn('No se encontró la tarea o no tiene el campo Nombre.')
            }
        } catch (error) {
            console.error('Error al realizar la solicitud:', error)
        }
    };
    

    // Cambiar entre vista de estudiante y profesor
    // const changeView = () => {
    //     setIsStudent(!isStudent)
    // }

    // const addArregloDeTareas = (nombre) => {
    //     setConversationArray([...conversationArray, nombre])
    // }
    const handleFetchTask = async (taskName) => {
        const apiGatewayURL = process.env.REACT_APP_VERCEL_API_GATEWAY
            ? `https://${process.env.REACT_APP_VERCEL_API_GATEWAY}`
            : 'http://127.0.0.1:2000';
    
        try {
            const response = await fetch(`${apiGatewayURL}/get/tarea/id`, { // Reemplaza con tu URL
                method: 'POST', // Cambia según el método de tu API
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name: taskName}), // Envía el nombre de la tarea
            })
    
            const data = await response.json();
            console.log('Respuesta del servidor:', data.tarea);
            localStorage.setItem("tarea", data.tarea)
        } catch (error) {
            console.error('Error en el fetch:', error);
        }
    }

    const handleThemeChange = (newTheme) => {
        setTheme(newTheme)
        localStorage.setItem('theme', newTheme)
    }

    // Mostrar las tareas o conversaciones en la barra lateral
    const displaySidebarListItems = () => {
        if (isStudent) {
            return [
                conversationArray.map((item, index) => (
                    <ListItem key={index}>
                        <ListItemButton
                            component={Link}
                            to="/essays"
                            onClick={() => {
                                setSelectedIndex(index); // Actualiza el índice seleccionado
                                handleFetchTask(item); // Realiza el fetch con el nombre de la tarea
                            }}
                            sx={{
                                fontWeight: selectedIndex === index ? 'bold' : 'normal', // Cambia el estilo si está seleccionado
                                backgroundColor: selectedIndex === index ? '#f0f0f0' : 'transparent', // Ejemplo: cambia color de fondo
                            }}
                        >
                            {item.length > 30 ? item.slice(0, 25) + "..." : item}
                        </ListItemButton>
                    </ListItem>
                ))
            ];
        }
        return [
            arregloDeTareas.map((_, index) => (
                <ListItem key={index}>
                    <ListItemButton component={Link} to="/">
                        {arregloDeTareas[index].length > 30 ? arregloDeTareas[index].slice(0, 25) + "..." : arregloDeTareas[index]}
                    </ListItemButton>
                </ListItem>
            ))
        ]
    }

    return (
        <Box sx={{display: 'flex'}}>
            <Drawer open={open} onClose={() => setOpen(false)} sx={{
                width: 240,
                flexShrink: 0,
                '& .MuiDrawer-paper': {
                    width: 240,
                    boxSizing: 'border-box',
                    flexDirection: 'column'
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
                }}>
                    <Tooltip title="Cerrar menú">
                        <IconButton sx={{mr: 'auto'}} color="neutral" aria-label="delete"
                                    onClick={() => setOpen(false)}>
                            <ViewSidebarRoundedIcon/>
                        </IconButton>
                    </Tooltip>
                    <Tooltip title={isStudent ? "Ingresar código de ensayo" : "Crear Tarea"}>
                        <IconButton sx={{ml: 'auto'}} color="neutral" aria-label="delete" onClick={() => {
                            if (isStudent) {
                                setOpenModal(true)
                            } else {
                                setOpen(true)
                                navigate("/essays/createhomework")
                            }
                        }
                        }>
                            <AddIcon/>
                        </IconButton>

                    </Tooltip>

                    <HomeworkCode
                        openModal={openModal}
                        setOpenModal={setOpenModal}
                        addToConversationArray={addToConversationArray}
                    />
                </Box>
                <Divider/>

                {/* Botón de Home */}
                <ListItem>
                    <ListItemButton
                        component={Link}
                        to="/"
                        sx={{borderRadius: 2}}
                    >
                        <Home sx={{
                            mr: 1,
                        }}/>

                        Home
                    </ListItemButton>
                </ListItem>

                <List>
                    {
                        displaySidebarListItems()

                    }
                </List>

                <Box
                    sx={{
                        display: 'flex',
                        gap: 1,
                        p: 1.5,
                        pb: 4,
                        borderTop: '3px solid',
                        borderColor: 'divider',
                        position: 'absolute',
                        bottom: 0,
                    }}
                >
                    {/* Muestra la foto del usuario si está disponible */}
                    <Box sx={{display: 'flex', alignItems: 'center', gap: 0.5}}>
                        <Avatar size="md" src={userInfo.picture} alt={userInfo.name}/>
                        {/* Mostrar la información almacenada en localStorage */}
                        <Typography sx={{
                            display: '-webkit-box',
                            overflow: 'hidden',
                            WebkitBoxOrient: 'vertical',
                            WebkitLineClamp: 1,
                        }} level="body-sm">
                            {userInfo.name}
                        </Typography>
                    </Box>
                    {/* Botón de cerrar sesión */}

                    <div ref={menuRef}>
                        <IconButton
                            aria-haspopup={true}
                            aria-controls={menuOpen ? 'drawer-menu' : undefined}
                            aria-expanded={menuOpen ? 'true' : undefined}
                            sx={{ml: 'auto'}}
                            slotProps={{root: {variant: 'outlined', color: 'neutral'}}}
                            onClick={() => setMenuOpen(!menuOpen)}
                        >
                            <MoreVert/>
                        </IconButton>

                        <Menu
                            id='drawer-menu'
                            sx={{zIndex: 1300}}
                            open={menuOpen}
                        >

                            <IconButton
                                aria-haspopup={true}
                                aria-controls={themeMenuOpen ? 'theme-menu' : undefined}
                                aria-expanded={themeMenuOpen ? 'true' : undefined}
                                disableRipple
                                sx={{
                                    ml: 'auto',
                                    width: '100%',
                                    justifyContent: 'flex-start',
                                    color: (theme) => theme.palette.mode === 'dark' ? '#fff' : '#000',
                                }}
                                slotProps={{root: {variant: 'outlined', color: 'neutral'}}}
                                onClick={(e) => {
                                    e.stopPropagation()
                                    setThemeMenuOpen(!themeMenuOpen)
                                }}
                            >
                                <PaletteRounded/>
                                <Typography variant="body1" sx={{marginLeft: 1}}>
                                    Tema
                                </Typography>
                            </IconButton>


                            <Menu sx={{zIndex: 1500}} open={themeMenuOpen}>
                                <MenuItem onClick={(e) => {
                                    e.stopPropagation()
                                    handleThemeChange('auto')
                                }}>
                                    <AutoAwesomeRounded/>
                                    <span style={{marginLeft: '8px', flexGrow: 1}}>Auto</span>
                                    {(theme === 'auto' || isAuto) && <CheckCircleRoundedIcon/>}
                                </MenuItem>
                                <MenuItem onClick={(e) => {
                                    handleThemeChange('light')
                                    e.stopPropagation()
                                }}>
                                    <LightModeRoundedIcon/>
                                    <span style={{marginLeft: '8px', flexGrow: 1}}>Claro</span>
                                    {theme === 'light' && !isAuto && <CheckCircleRoundedIcon/>}
                                </MenuItem>
                                <MenuItem onClick={(e) => {
                                    e.stopPropagation()
                                    handleThemeChange('dark')
                                }}>
                                    <DarkModeRoundedIcon/>
                                    <span style={{marginLeft: '8px', flexGrow: 1}}>Oscuro</span>
                                    {theme === 'dark' && !isAuto && <CheckCircleRoundedIcon/>}
                                </MenuItem>
                            </Menu>

                            {/*<MenuItem*/}
                            {/*    component={Link}*/}
                            {/*    to={"/"}*/}
                            {/*    onClick={() => {*/}
                            {/*        setMenuOpen(false)*/}
                            {/*        changeView()*/}
                            {/*    }}*/}
                            {/*>*/}
                            {/*    {isStudent ? "Cambiar a profesor" : "Cambiar a alumno"}*/}
                            {/*</MenuItem>*/}

                            <MenuItem onClick={() => {
                                setMenuOpen(false)
                                localStorage.clear()
                                navigate('/auth')
                            }}
                            >
                                Cerrar sesión
                            </MenuItem>
                        </Menu>
                    </div>
                </Box>
            </Drawer>
            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    transition: 'margin 0.3s ease',
                    marginLeft: open ? `0px` : '-250px',
                }}
            >
                {!open && (

                    <Tooltip title="Abrir menú">
                        <IconButton sx={{
                            position: 'absolute',
                            top: 6,
                            left: 6,
                        }} color="neutral" onClick={() => setOpen(true)}>
                            <ViewSidebarRoundedIcon/>
                        </IconButton>
                    </Tooltip>
                )}
                <Outlet/>
            </Box>
        </Box>
    )
}

export const useClickOutside = (ref, callback) => {
    const handleClick = (event) => {
        if (ref.current && !ref.current.contains(event.target)) {
            callback()
        }
    }

    useEffect(() => {
        document.addEventListener('click', handleClick)

        return () => {
            document.removeEventListener('click', handleClick)
        }
    })
}

export default Layout
