import Box from "@mui/material/Box"
import Avatar from "@mui/material/Avatar"
import React, {useEffect, useState} from "react"
import {useNavigate} from "react-router-dom"
import Typography from "@mui/material/Typography";

// UserInfo es un componente que muestra la información del usuario
const UserInfo = () => {
    const [userInfo, setUserInfo] = useState({name: "", email: "", picture: ""})
    const navigate = useNavigate()

    useEffect(() => {
        const storedUserInfo = localStorage.getItem('userInfo')
        if (storedUserInfo) setUserInfo(JSON.parse(storedUserInfo))
        else navigate('/auth')
    }, [])

    return (
        <Box>
            <Box sx={{
                width: "100%",
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                justifyContent: "center",
                marginTop: 5,
                marginBottom: 3
            }}>
                <Avatar
                    sx={{
                        width: 75,
                        height: 75
                    }}
                    src={userInfo.picture}
                    alt={userInfo.name}
                />

                <Box sx={{
                    display: 'flex',
                    flexDirection: "column",
                    marginLeft: 2,
                    columnGap: 0,
                    justifyContent: "center",
                }}>
                    <Typography variant="h6" fontWeight="bold">{userInfo.name}</Typography>
                    <Typography fontStyle="italic" color="gray">{userInfo.email}</Typography>
                </Box>
            </Box>
        </Box>
    )
}

export default UserInfo