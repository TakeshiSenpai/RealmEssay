import React from 'react';
import ReactDOM from 'react-dom/client';

import {BrowserRouter, Routes, Route} from "react-router-dom";
import reportWebVitals from './reportWebVitals';
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Auth from './pages/Auth';
import Tarea from "./pages/Tarea";
import {createTheme, CssBaseline, ThemeProvider} from "@mui/material";

import './index.css'

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
    }
})

function App3() {
    return (
        <BrowserRouter>
            <ThemeProvider theme={darkTheme}>
                <CssBaseline/>
                <Routes>
                    <Route path="/" element={<Layout/>}>
                        <Route index element={<Home/>}/>
                        <Route path="/tarea" element={<Tarea/>}/>
                    </Route>
                    <Route path="/auth" element={<Auth/>}/>
                </Routes>
            </ThemeProvider>
        </BrowserRouter>
    )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App3/>);
reportWebVitals();
