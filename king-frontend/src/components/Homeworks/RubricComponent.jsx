import React from 'react'
import Box from "@mui/material/Box"
import Button from "@mui/material/Button";
import {TextField} from "@mui/material";
import {grey} from "@mui/material/colors";
import {Add, Delete} from "@mui/icons-material";
import Typography from "@mui/material/Typography";

// RubricComponent es un componente que permite al profesor crear una rúbrica
const RubricComponent = ({parameters, setParameters, error,setError}) => {

    console.log(error)

    const addNewParameter = () => {
        setParameters([...parameters, {
            title: "",
            description: "",
            totalValue: 0,
            criterias: [],
            error: false
        }])
    }

    const apiGatewayURL = process.env.REACT_APP_VERCEL_API_GATEWAY
                ? `https://${process.env.REACT_APP_VERCEL_API_GATEWAY}`
                : 'http://127.0.0.1:2000'
    const handleParameterChange = (index, field, value) => {
        //const newParameters = [...parameters]
        const newParameters = parameters.map((param, i) =>
            i === index ? {...param, [field]: field === 'totalValue' ? parseInt(value, 10) || 0 : value} : param
        );

        if (field === 'totalValue') {
            const intValue = parseInt(value, 10)
            if (isNaN(intValue)) {
                newParameters[index].error = true
                newParameters[index][field] = value
            } else {
                newParameters[index].error = intValue === 0
                newParameters[index][field] = intValue
            }
        } else {
            newParameters[index][field] = value
        }

        setParameters(newParameters)
    }

    const removeParameter = (index) => {
        const newParameters = parameters.filter((_, i) => i !== index)
        setParameters(newParameters)
    }

    const addNewCriteria = (index) => {
        const newParameters = [...parameters]
        newParameters[index].criterias.push({
            rating: "",
            description: "",
            partialValue: 0,
            error: false
        })
        setParameters(newParameters)
    }

    const handleSubmit = async () => {
        if (parameters.length === 0) {
            setError(true)
            return
        }

        const newParameters = parameters.map(param => {
            if (param.totalValue === 0) {
                return {...param, error: true}
            }
            return param
        })

        const updatedParameters = newParameters.map(param => {
            const updatedCriterias = param.criterias.map(criteria => {
                return {...criteria, error: !criteria.rating.trim() || !criteria.description.trim()}
            })
            return {...param, criterias: updatedCriterias}
        })

        setParameters(updatedParameters)

        if (updatedParameters.some(param => param.error)) return
        if (updatedParameters.some(param => param.criterias.some(criteria => criteria.error))) return

        // Parámetros sin la propiedad error
        const sentParameters = updatedParameters.map(param => {
            const {error, ...rest} = param
            const newCriterias = rest.criterias.map(criteria => {
                const {error, ...rest} = criteria
                return rest
            })
            return {...rest, criterias: newCriterias}
        })

        // Todo bien, enviar rúbrica
        try {
            const response = await fetch(`${apiGatewayURL}/tarea/rubrica`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({rubrica: sentParameters})
            })

            const data = await response.json()
            alert(data.message)
            console.log(data.message)
        } catch (error) {
            alert(`Error al enviar la rúbrica: ${error.message}`)
        }
    }

    return (

        <Box sx={{paddingTop: -5, paddingX: 2}}>
            <h1>Rúbrica</h1>

            <Box sx={{display: 'flex', justifyContent: 'space-between', alignItems: 'center',}}>
                {(parameters.length > 0) &&
                    <p>Total de puntos: <strong>{parameters.reduce((sum, param) => sum + param.totalValue, 0)}</strong>
                    </p>}
            </Box>


            {parameters.map((parameter, index) => (
                <Box
                    key={index}
                    sx={{
                        borderRadius: 3,
                        border: '1px solid',
                        borderColor: grey[500],
                        paddingX: 2,
                        paddingBottom: 2,
                        marginBottom: 2
                    }}
                >
                    <Box sx={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        marginBottom: '0px'
                    }}
                    >
                        <h3>Parámetro {index + 1}</h3>
                        <Button
                            variant="outlined"
                            color="error"
                            sx={{minWidth: 'auto', padding: '5px'}}
                            onClick={() => removeParameter(index)}
                        >
                            <Delete/>
                        </Button>
                    </Box>

                    <Box sx={{display: 'flex', gap: 2}}>
                        <TextField
                            label="Título"
                            value={parameter.title}
                            onChange={(e) => {
                                handleParameterChange(index, 'title', e.target.value)

                            }}
                            sx={{flex: 7}}
                            margin="normal"
                            error={parameter.error && !parameter.title.trim()}
                            helperText={parameter.error && !parameter.title.trim() ? "Este campo es requerido" : ""}
                            size="small"
                        />

                        <TextField
                            label="Valor Total"
                            value={parameter.totalValue}
                            onChange={(e) => {
                                handleParameterChange(index, 'totalValue', e.target.value)

                            }}
                            sx={{flex: 3}}
                            margin="normal"
                            size="small"
                            error={parameter.error}
                            helperText={parameter.error ? "No puede ser cero" : ""}
                            inputProps={{inputMode: 'numeric', pattern: '[0-9]*'}}
                        />
                    </Box>

                    <TextField
                        label="Descripción"
                        value={parameter.description}
                        onChange={(e) => {
                            handleParameterChange(index, 'description', e.target.value)

                        }}
                        fullWidth
                        margin="normal"
                        size="small"
                    />

                    <Box sx={{display: 'flex', alignItems: 'center', gap: 1}}>
                        <h3>Criterios</h3>
                        <Button
                            variant="outlined"
                            onClick={() => addNewCriteria(index)}
                            sx={{minWidth: 'auto', padding: 0}}
                        >
                            <Add/>
                        </Button>
                    </Box>

                    {/* Criterias */}
                    <Box sx={{display: 'flex', overflowX: 'auto', gap: 2, maxWidth: '100%', whiteSpace: 'wrap'}}>
                        {parameter.criterias.map((criteria, criteriaIndex) => (
                            <Box
                                key={criteriaIndex}
                                sx={{
                                    borderRadius: 2,
                                    border: '1px solid',
                                    borderColor: grey[400],
                                    paddingX: 2,
                                    paddingY: '1px',
                                    minWidth: 300
                                }}
                            >
                                <Box sx={{display: 'flex', gap: 2}}>
                                    <TextField
                                        label="Evalución"
                                        value={criteria.rating}
                                        onChange={(e) => {
                                            const newParameters = [...parameters]
                                            newParameters[index].criterias[criteriaIndex].rating = e.target.value
                                            setParameters(newParameters)

                                        }}
                                        sx={{flex: 6}}
                                        fullWidth
                                        margin="normal"
                                        size="small"
                                        error={criteria.error && !criteria.rating.trim()}
                                        helperText={criteria.error && !criteria.rating.trim() ? "Este campo es requerido" : ""}
                                    />

                                    <TextField
                                        label="Valor Parcial"
                                        value={criteria.partialValue}
                                        onChange={(e) => {
                                            const newParameters = [...parameters]
                                            newParameters[index].criterias[criteriaIndex].partialValue = parseInt(e.target.value, 10) || 0
                                            setParameters(newParameters)

                                        }}
                                        onBlur={(e) => {
                                            if (parseInt(e.target.value, 10) > parameter.totalValue) {
                                                const newParameters = [...parameters]
                                                newParameters[index].criterias[criteriaIndex].partialValue = parameter.totalValue
                                                setParameters(newParameters)
                                            }
                                        }}
                                        sx={{flex: 4}}
                                        fullWidth
                                        margin="normal"
                                        size="small"
                                        inputProps={{inputMode: 'numeric', pattern: '[0-9]*'}}
                                    />
                                </Box>

                                <TextField
                                    label="Descripción"
                                    value={criteria.description}
                                    onChange={(e) => {
                                        const newParameters = [...parameters]
                                        newParameters[index].criterias[criteriaIndex].description = e.target.value
                                        setParameters(newParameters)

                                    }}
                                    fullWidth
                                    margin="normal"
                                    size="small"
                                    multiline
                                    rows={4}
                                    error={criteria.error && !criteria.description.trim()}
                                    helperText={criteria.error && !criteria.description.trim() ? "Este campo es requerido" : ""}
                                />

                                <Box sx={{display: 'flex', justifyContent: 'flex-end', paddingBottom: 1}}>
                                    <Button
                                        variant="outlined"
                                        color="error"
                                        sx={{minWidth: 'auto', padding: '5px'}}
                                        onClick={() => {
                                            const newParameters = [...parameters]
                                            newParameters[index].criterias.splice(criteriaIndex, 1)
                                            setParameters(newParameters)
                                        }}
                                    >
                                        <Delete/>
                                    </Button>
                                </Box>
                            </Box>
                        ))}
                    </Box>
                </Box>
            ))}

            {(error && !parameters.length > 0) &&
                <Typography
                    sx={{
                        color: (theme) => theme.palette.colors.errorText
                    }}
                >
                    Debe añadir al menos un criterio antes de enviar.
                </Typography>
            }

            <Box sx={{display: 'flex', justifyContent: 'space-between', marginY: 2}}>
                <Button
                    variant="outlined"
                    onClick={addNewParameter}
                >
                    Añadir Parámetro
                </Button>

            </Box>
        </Box>

    )
}

export default RubricComponent