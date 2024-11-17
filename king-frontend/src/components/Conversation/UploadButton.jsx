import Box from "@mui/material/Box"
import {useDropzone} from "react-dropzone"
import {useCallback, useState} from "react"
import {useTheme} from "@mui/material"
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import {DeleteRounded, Send} from "@mui/icons-material";

// UploadButton es un componente que permite al estudiante subir un archivo .pdf o .txt
const UploadButton = ({setShowConversation}) => {

    const [file, setFile] = useState(null)
    const [error, setError] = useState(null)

    const onDrop = useCallback(file => {
        if (file[0]) setFile(file[0])
        setError(null)
    }, [])
    const studentUrl = process.env.REACT_APP_VERCEL_HOMEWORK_STUDENT
                ? `https://${process.env.REACT_APP_VERCEL_HOMEWORK_STUDENT}`
                : 'http://127.0.0.1:2004';

    // Configuración del dropzone para aceptar archivos .pdf y .txt
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

            //console.log(process.env);
            //console.log(process.env.development);
            //console.log(process.env.production);
            const reader = new FileReader()
            reader.onabort = () => console.log('file reading was aborted')
            reader.onerror = () => console.log('file reading has failed')
            reader.onload = async () => {
                try {
                    const arrayBuffer = reader.result;

                    const binaryString = Array.from(new Uint8Array(arrayBuffer))
                        .map(byte => String.fromCharCode(byte))
                        .join('');

                    const response = await fetch(`${studentUrl}/submit_essay`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            fileName: file.name,
                            fileData: btoa(binaryString),
                        })
                    })

                    if (!response.ok) {
                        const data = await response.json()
                        setError(data.message)
                        return
                    }

                    setShowConversation(true)
                } catch (error) {
                    setError(error.message)
                }
            }

            reader.readAsArrayBuffer(file)
        } catch (error) {
            setError(error.message)
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
                    borderColor: (theme) => isDragActive ? theme.palette.primary.main : theme.palette.text.primary,
                    maxWidth: '450px',
                    margin: '0 auto'
                }}>
                    <img
                        src={`${process.env.PUBLIC_URL}/res/PDF-TXT(${useTheme().palette.mode === 'dark' ? 'dark' : 'light'}).png`}
                        alt="Archivos permitidos: .pdf, .txt"
                        style={{
                            width: '90%',
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
                                cursor: 'default',
                                paddingBottom: '10px'
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
                                    setError(null)
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

                    {error != null && (
                        <Typography sx={{
                            backgroundColor: 'red',
                            borderRadius: '8px',
                            padding: '5px',
                            display: 'inline-block',
                            color: 'white',
                            width: '100%'
                        }}>
                            {error.toString()}
                        </Typography>
                    )}
                </Box>
            </div>
        </Box>
    )
}

export default UploadButton
