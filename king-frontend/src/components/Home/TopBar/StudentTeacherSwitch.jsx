import {styled, Switch} from "@mui/material"
import {useIsStudent} from "../../IsStudentProvider"

// StudentTeacherSwitch es un componente que representa un switch para cambiar entre la vista de estudiante y profesor
const StudentTeacherSwitch = () => {
    const {isStudent, setIsStudent} = useIsStudent()
    return (
        <MaterialUISwitch
            checked={isStudent}
            onChange={() => setIsStudent(!isStudent)}
            sx={{
                marginLeft: 2,
                scale: 1.2,
                marginTop: '2px'
            }}
        />
    )
}

// MaterialUISwitch es un componente que representa un switch con estilos personalizados
// https://mui.com/material-ui/react-switch/#customization
const MaterialUISwitch = styled(Switch)(({theme}) => ({
    width: 62,
    height: 34,
    padding: 7,
    '& .MuiSwitch-switchBase': {
        margin: 1,
        padding: 0,
        transform: 'translateX(6px)',
        '&.Mui-checked': {
            color: '#fff',
            transform: 'translateX(22px)',
            '& .MuiSwitch-thumb:before': {
                backgroundImage: `url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 256 256"><path fill="white" d="m226.53 56.41l-96-32a8 8 0 0 0-5.06 0l-96 32A8 8 0 0 0 24 64v80a8 8 0 0 0 16 0V75.1l33.59 11.19a64 64 0 0 0 20.65 88.05c-18 7.06-33.56 19.83-44.94 37.29a8 8 0 1 0 13.4 8.74C77.77 197.25 101.57 184 128 184s50.23 13.25 65.3 36.37a8 8 0 0 0 13.4-8.74c-11.38-17.46-27-30.23-44.94-37.29a64 64 0 0 0 20.65-88l44.12-14.7a8 8 0 0 0 0-15.18ZM176 120a48 48 0 1 1-86.65-28.45l36.12 12a8 8 0 0 0 5.06 0l36.12-12A47.9 47.9 0 0 1 176 120m-48-32.43L57.3 64L128 40.43L198.7 64Z"/></svg>')`,
            },
            '& + .MuiSwitch-track': {
                opacity: 1,
                backgroundColor: '#aab4be',
                ...theme.applyStyles('dark', {
                    backgroundColor: '#8796A5',
                }),
            },
        },
    },
    '& .MuiSwitch-thumb': {
        backgroundColor: '#6a55af',
        width: 32,
        height: 32,
        '&::before': {
            content: "''",
            position: 'absolute',
            width: '100%',
            height: '100%',
            left: 0,
            top: 0,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundImage: `url('data:image/svg+xml;utf8,<svg width="20" height="20" fill="white" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path d="M311.6 592.8c-80.4 0-145.7-65.4-145.7-145.7s65.4-145.7 145.7-145.7S457.3 366.7 457.3 447s-65.4 145.8-145.7 145.8z m0-243.6c-53.9 0-97.8 43.9-97.8 97.8s43.9 97.8 97.8 97.8 97.8-43.9 97.8-97.8-43.9-97.8-97.8-97.8zM556.5 902.6h-47.9V758.3c0-56.4-45.9-102.3-102.3-102.3H216.8c-56.4 0-102.3 45.9-102.3 102.3v144.3H66.6V758.3C66.6 675.4 134 608 216.8 608h189.4c82.8 0 150.2 67.4 150.2 150.2v144.4z" /><path d="M957.4 798.7H657.8v-47.9h251.7V159.5H272.4v107.9h-47.9V111.6h732.9z" /><path d="M510.715 892.736l184.668-411.903 43.709 19.596-184.668 411.903z"/></svg>')`,
        }
    },
    '& .MuiSwitch-track': {
        opacity: 1,
        backgroundColor: '#aab4be',
        borderRadius: 20 / 2,
        ...theme.applyStyles('dark', {
            backgroundColor: '#8796A5',
        }),
    },
}))

export default StudentTeacherSwitch