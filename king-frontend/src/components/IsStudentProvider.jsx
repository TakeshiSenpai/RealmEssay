// IsStudentProvider.jsx es un componente que provee un contexto para saber si el usuario es estudiante o no.
// Con esto podemos acceder a la misma información en cualquier parte de la aplicación.

import React, {createContext, useContext, useState} from 'react'

const IsStudentContext = createContext()

// Crear el proveedor del contexto
export const IsStudentProvider = ({ children }) => {
    const [isStudent, setIsStudent] = useState(false)

    return (
        <IsStudentContext.Provider value={{ isStudent, setIsStudent }}>
            {children}
        </IsStudentContext.Provider>
    )
}

// Crear un hook para acceder fácilmente al contexto
export const useIsStudent = () => {
    return useContext(IsStudentContext)
}