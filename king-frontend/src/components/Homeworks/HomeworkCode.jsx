import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import Stack from "@mui/material/Stack";
import FormControl from "@mui/material/FormControl";
import Input from "@mui/material/Input";
import {Button, Dialog} from "@mui/material";
import React from "react";

const HomeworkCode = ({openModal, setOpenModal, addToConversationArray}) => {
    return <Dialog open={openModal} onClose={() => setOpenModal(false)}>
        <DialogContent>
            <DialogTitle fontWeight="bold">Ingresa el código de chat</DialogTitle>
            <DialogContent>El código debe ser proporcionado por su profesor.</DialogContent>
            <form
                onSubmit={(event) => {
                    event.preventDefault()
                    setOpenModal(false)
                    const formData = new FormData(event.currentTarget)
                    const formJson = Object.fromEntries(formData.entries())
                    addToConversationArray(formJson.code)
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
}

export default HomeworkCode