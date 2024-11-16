import Box from "@mui/material/Box"
import RealmEssayLogo from "./RealmEssayLogo"
import SearchBar from "./SearchBar";
import StudentTeacherSwitch from "./StudentTeacherSwitch"

// TopBar es un componente que representa la barra superior de la página de Home
const TopBar = ({setSearchString}) => {
    return (
        <Box sx={{
            display: 'flex',
            alignItems: 'top',
            marginTop: 2
        }}>
            <RealmEssayLogo/>
            <Box sx={{flexGrow: 1}}/>
            <SearchBar setSearchString={setSearchString}/>
            <StudentTeacherSwitch />
        </Box>
    )
}

export default TopBar