import React, {useEffect} from 'react'
import ReactDOM from 'react-dom/client'
 
import {BrowserRouter, Route, Routes} from "react-router-dom"
import reportWebVitals from './reportWebVitals'
import Layout from "./pages/Layout"
import { TalkTo } from "./pages/TalkTo"
import Auth from './pages/Auth'
import Homework from "./pages/Homework"
import {createTheme, CssBaseline, ThemeProvider} from "@mui/material"

import './index.css'

function App3() {
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

        // const themeColor = theme === 'dark' ? '#6a55af' : 'rgb(248,246,252)'
        document.querySelector('meta[name="theme-color"]').setAttribute('content', themeColor)

        return () => mediaQuery.removeEventListener('change', handleChange)
    }, [isAuto, theme])

    const handleThemeChange = (newTheme) => {
        setIsAuto(newTheme === 'auto')
        setTheme(newTheme)
    }

    return (
        <BrowserRouter>
            <ThemeProvider theme={getTheme()}>
                <CssBaseline/>
                <Routes>
                    <Route path="/" element={<Layout setTheme={handleThemeChange} theme={theme} isAuto={isAuto}/>}>
                        <Route index element={<TalkTo/>}/>
                        <Route path="/createhomework" element={<Homework/>}/>
                    </Route>
                    <Route path="/auth" element={<Auth/>}/>
                </Routes>
            </ThemeProvider>
        </BrowserRouter>
    )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<App3/>)
reportWebVitals()
