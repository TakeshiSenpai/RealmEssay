import Box from "@mui/material/Box"
import {useDropzone} from "react-dropzone"
import {useCallback, useState} from "react"
import {useTheme} from "@mui/material"
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import {DeleteRounded, Send} from "@mui/icons-material";

const UploadButton = ({setShowConversation}) => {

    const [file, setFile] = useState(null)

    const onDrop = useCallback(file => {
        if (file[0]) setFile(file[0])
    }, [])

    const {getRootProps, getInputProps, isDragActive} = useDropzone({
        onDrop: onDrop,
        accept: {
            'text/plain': '.txt',
            'application/pdf': '.pdf'
        }
    })

    // Enviar el archivo a la IA, si sale bien, mostrar la conversación.
    const handleSubmission = async () => {
        try {
            // (no sé como funciona la IA, para mandarle el contenido del archivo)
            const reader = new FileReader()
            reader.onabort = () => console.log('file reading was aborted')
            reader.onerror = () => console.log('file reading has failed')
            reader.onload = () => {
                // Do whatever you want with the file contents
                const binaryStr = reader.result
                console.log(binaryStr)
            }

            reader.readAsArrayBuffer(file)
            // await enviar ensayo a la IA
            setShowConversation(true)
        } catch (error) {
            console.log(error)
        }
    }

    return (
        <Box sx={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            height: '100vh',
            textAlign: 'center',
            width: '100%',
        }}>
            <div
                {...getRootProps()}
                style={{
                    width: '50%',
                    margin: '0 auto',
                }}
            >
                <input {...getInputProps()} />
                <Box sx={{
                    cursor: 'pointer',
                    border: '2px dashed',
                    borderRadius: '10px',
                    textAlign: 'center',
                    padding: '20px',
                    borderColor: (theme) => isDragActive ? theme.palette.primary.main : theme.palette.text.primary
                }}>
                    <img
                        src={`${process.env.PUBLIC_URL}/res/PDF-TXT(${useTheme().palette.mode === 'dark' ? 'dark' : 'light'}).png`}
                        alt="Archivos permitidos: .pdf, .txt"
                        style={{
                            width: '90%'
                        }}
                    />

                    <h3>
                        {isDragActive ? 'Suelta el archivo aquí...' : 'Arrastra o selecciona un archivo.'}
                    </h3>

                    {file != null && (
                        <Box
                            sx={{
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'space-between',
                                gap: '10px',
                                cursor: 'default'
                            }}
                            onClick={(e) => e.stopPropagation()}
                        >
                            <Typography sx={{
                                backgroundColor: 'grey.200',
                                borderRadius: '8px',
                                padding: '5px',
                                display: 'inline-block',
                                color: 'black',
                                width: '100%'
                            }}>
                                {file.name}
                            </Typography>

                            <IconButton sx={{
                                border: '1px red solid',
                                padding: '5px',
                                borderRadius: '8px',
                                color: 'red'
                            }}>
                                <DeleteRounded onClick={(e) => {
                                    e.stopPropagation()
                                    setFile(null)
                                }}/>
                            </IconButton>

                            <IconButton sx={{
                                border: (theme) => `1px ${theme.palette.primary.main} solid`,
                                padding: '5px',
                                borderRadius: '8px',
                                color: (theme) => theme.palette.primary.main
                            }}>
                                <Send onClick={async (e) => {
                                    e.stopPropagation()
                                    await handleSubmission()
                                }}/>
                            </IconButton>
                        </Box>
                    )}

                </Box>
            </div>
        </Box>
    )
}

export default UploadButton;
