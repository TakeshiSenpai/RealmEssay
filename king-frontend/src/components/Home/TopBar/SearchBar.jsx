import {InputAdornment, TextField} from "@mui/material"
import {Search} from "@mui/icons-material"

const SearchBar = ({setSearchString}) => {
    return (
        <TextField
            type="text"
            placeholder="Buscar..."
            onChange={(e) => setSearchString(e.target.value)}
            size="small"
            sx={{
                backgroundColor: (theme) => theme.palette.primary.secondary,
                borderRadius: '8px',
                '& .MuiOutlinedInput-root': {
                    borderRadius: '8px',
                },
            }}
            slotProps={{
                input: {
                    startAdornment: (
                        <InputAdornment position="start">
                            <Search/>
                        </InputAdornment>
                    )
                }
            }}
        />
    )
}

export default SearchBar