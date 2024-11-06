import React, {useEffect} from 'react'
import ReactDOM from 'react-dom/client'
import {BrowserRouter, Route, Routes, useNavigate} from "react-router-dom"
import reportWebVitals from './reportWebVitals'
import Layout from "./pages/Layout"
import StudentAIChat from "./pages/StudentAIChat"
import Auth from './pages/Auth'
import Homework from "./pages/Homework"
import {createTheme, CssBaseline, ThemeProvider} from "@mui/material"

import './index.css'

// App3 es el componente principal de la aplicación
function App3() {
    const token = localStorage.getItem('token')
    const navigate = useNavigate()
    useEffect(() => {
        if (!token) {
            navigate('/auth')
        }
    }, [token, navigate])

    const [theme, setTheme] = React.useState(localStorage.getItem('theme') || 'auto')
    const [isAuto, setIsAuto] = React.useState(theme === 'auto')

    const lightTheme = createTheme({
        palette: {
            mode: 'light',
            background: {
                default: '#f5f5f5',
                paper: 'rgb(248,246,252)',
            },
            primary: {
                main: '#6a55af'
            },
            colors: {
                errorText: 'red',
                textGradient: "linear-gradient(to right, #a195d0, #6a55af)",
                iaBackground: 'rgb(239, 236, 244)',
            }
        }
    })

    const darkTheme = createTheme({
        palette: {
            mode: 'dark',
            background: {
                default: '#2a2737',
                paper: '#191821'
            },
            primary: {
                main: '#6a55af',
            },
            colors: {
                errorText: '#cb5f7d',
                textGradient: "linear-gradient(to right, #a195d0, #6a55af)",
                iaBackground: 'rgba(35, 30, 52, 1)',
            }
        }
    })

    const getTheme = () => {
        if (isAuto) return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? darkTheme : lightTheme
        return theme === 'dark' ? darkTheme : lightTheme
    }

    useEffect(() => {
        localStorage.setItem('theme', theme)
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
        const handleChange = () => {
            if (isAuto) {
                setTheme(mediaQuery.matches ? 'dark' : 'light')
            }
        }
        mediaQuery.addEventListener('change', handleChange)

        let themeColor
        if (isAuto) themeColor = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? '#6a55af' : 'rgb(248,246,252)'
        else themeColor = theme === 'dark' ? '#6a55af' : 'rgb(248,246,252)'

        document.querySelector('meta[name="theme-color"]').setAttribute('content', themeColor)

        return () => mediaQuery.removeEventListener('change', handleChange)
    }, [isAuto, theme])

    const handleThemeChange = (newTheme) => {
        setIsAuto(newTheme === 'auto')
        setTheme(newTheme)
    }

    return (
        <ThemeProvider theme={getTheme()}>
            <CssBaseline/>
            <Routes>
                <Route path="/" element={<Layout setTheme={handleThemeChange} theme={theme} isAuto={isAuto}/>}>
                    <Route index element={<StudentAIChat/>}/>
                    <Route path="/createhomework" element={<Homework/>}/>
                </Route>
                <Route path="/auth" element={<Auth/>}/>
            </Routes>
        </ThemeProvider>
    )
}

// ProtectedAppWrapper se encarga de envolver la aplicación para poder utilizar useNavigate.
// Esto es necesario para redirigir al usuario a la página de autenticación si no ha iniciado sesión.
const ProtectedAppWrapper = () => (
    <BrowserRouter>
        <App3 />
    </BrowserRouter>
)

// Se renderiza la aplicación en el elemento con id 'root'
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<ProtectedAppWrapper />)
reportWebVitals()