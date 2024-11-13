import Box from "@mui/material/Box"
import React, {useEffect, useState} from "react"
import TopBar from "../components/Home/TopBar/TopBar"
import UserInfo from "../components/Home/UserInfo"
import StudentEssays from "../components/Home/Student Essays/StudentEssays"
import TeacherHome from "../components/Home/Teacher/TeacherHome"
import {useIsStudent} from "../components/IsStudentProvider"

// RealmEssayHome es un componente que representa la página principal de RealmEssay de un usuario autenticado
const RealmEssayHome = () => {
    const [searchString, setSearchString] = useState('')
    const {isStudent} = useIsStudent()
    const [essays, setEssays] = useState([])

    useEffect(() => {
        const getEssays = async () => {
            try {
                const response = await fetch("https://67344830a042ab85d1197a61.mockapi.io/fakeAPI/essays")
                const data = await response.json()
                setEssays(data)
            } catch (error) {
                console.log(error)
            }
        }

        getEssays().catch()
    }, [])

    useEffect(() => {
        console.log(searchString)
    }, [searchString])

    useEffect(() => {
        console.log(isStudent)
    }, [isStudent])

    return (
        <Box sx={{
            height: '100dvh',
            marginX: 2,
        }}>
            <TopBar setSearchString={setSearchString}/>
            <UserInfo/>

            {isStudent && (
                <StudentEssays searchString={searchString} essays={essays}/>
            )}

            {!isStudent && (
                <TeacherHome />
            )}
        </Box>
    )
}

export default RealmEssayHome