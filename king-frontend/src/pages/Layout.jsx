import {Button, Dialog, Divider, ListItemButton} from '@mui/material'
import Drawer from '@mui/material/Drawer'
import React, {useEffect, useRef, useState} from 'react'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import IconButton from '@mui/material/IconButton'
import Avatar from '@mui/material/Avatar'
import DialogTitle from '@mui/material/DialogTitle'
import DialogContent from '@mui/material/DialogContent'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import ViewSidebarRoundedIcon from '@mui/icons-material/ViewSidebarRounded'
import {Link, Outlet, useNavigate} from "react-router-dom"
import Tooltip from '@mui/material/Tooltip'
import AddIcon from '@mui/icons-material/Add'
import FormControl from '@mui/material/FormControl'
import Input from '@mui/material/Input'
import Stack from '@mui/material/Stack'
import LightModeRoundedIcon from '@mui/icons-material/LightModeRounded'
import Menu from '@mui/material/Menu'
import MenuItem from '@mui/material/MenuItem'
import MoreVert from '@mui/icons-material/MoreVert'
import DarkModeRoundedIcon from '@mui/icons-material/DarkModeRounded'
import {AutoAwesomeRounded, PaletteRounded} from "@mui/icons-material"
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded";

// Layout es un componente que representa la estructura de la página
const Layout = ({theme, setTheme, isAuto}) => {
    const [open, setOpen] = useState(true)
    const [openModal, setOpenModal] = useState(false)
    const [userInfo, setUserInfo] = useState({name: '', institution: '', picture: ''})
    const [conversationArray, setConversationArray] = useState(["Home"])
    const [arregloDeTareas, setArregloDeTareas] = useState(["Primera Tarea"])

    const navigate = useNavigate()
    const [isStudent, setIsStudent] = useState(true)

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

            console.log(parsedUserInfo)

            setUserInfo({
                name: parsedUserInfo.name,
                institution: parsedUserInfo.institution,
                picture: parsedUserInfo.picture
            })
        }

        const savedTheme = localStorage.getItem('theme')
        if (savedTheme) setTheme(savedTheme)
    }, [])

    const addToConversationArray = (code) => {
        setConversationArray([...conversationArray, code])
    }

    // Cambiar entre vista de estudiante y profesor
    const changeView = () => {
        setIsStudent(!isStudent)
    }

    const addArregloDeTareas = (nombre) => {
        setConversationArray([...conversationArray, nombre])
    }

    const handleThemeChange = (newTheme) => {
        setTheme(newTheme)
        localStorage.setItem('theme', newTheme)
    }

    // Mostrar las tareas o conversaciones en la barra lateral
    const displaySidebarListItems = () => {
        if (isStudent) {
            return [
                conversationArray.map((_, index) => (
                    <ListItem key={index}>
                        <ListItemButton component={Link} to="/">
                            {conversationArray[index].length > 30 ? conversationArray[index].slice(0, 25) + "..." : conversationArray[index]}
                        </ListItemButton>
                    </ListItem>
                ))
            ]
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
                    <Tooltip title={isStudent ? "Ingresar code de conversacion" : "Crear Tarea"}>
                        <IconButton sx={{ml: 'auto'}} color="neutral" aria-label="delete" component={Link}
                                    to={isStudent ? "/" : "/Tarea"} onClick={isStudent
                            ? () => setOpenModal(true) : () => setOpen(true)}>
                            <AddIcon/>
                        </IconButton>

                    </Tooltip>
                    <Dialog open={openModal} onClose={() => setOpenModal(false)}>
                        <DialogContent>
                            <DialogTitle>Ingresa el código de chat</DialogTitle>
                            <DialogContent>El código debe ser proporcionado por su profesor</DialogContent>
                            <form
                                onSubmit={(event) => {
                                    event.preventDefault()
                                    setOpenModal(false)
                                    const formData = new FormData(event.currentTarget)
                                    const formJson = Object.fromEntries(formData.entries())
                                    addToConversationArray(formJson.code)
                                    console.log(conversationArray)
                                }}
                            >
                                <Stack spacing={2}>
                                    <FormControl>
                                        <Input autoFocus required name="code"/>
                                    </FormControl>
                                    <Button type="submit" variant='contained'>Enviar</Button>
                                </Stack>
                            </form>
                        </DialogContent>
                    </Dialog>
                </Box>
                <Divider/>
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

                            <MenuItem
                                component={Link}
                                to={!isStudent ? "/" : "/createhomework"}
                                onClick={() => {
                                    setMenuOpen(false)
                                    changeView()
                                }}
                            >
                                {isStudent ? "Cambiar a profesor" : "Cambiar a alumno"}
                            </MenuItem>

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