import React from 'react'
import {GoogleLogin, GoogleOAuthProvider} from '@react-oauth/google'
import Button from '@mui/material/Button'
import GoogleIcon from '@mui/icons-material/Google'
import {useNavigate} from 'react-router-dom'

// GoogleButton es un componente que permite al usuario iniciar sesión con Google
const GoogleButton = () => {
    const navigate = useNavigate()
    const authURL =  process.env.REACT_APP_VERCEL_AUTHENTICATION
    ? `https://${process.env.REACT_APP_VERCEL_AUTHENTICATION}`
    : 'http://127.0.0.1:2001'
    // Maneja el éxito de la autenticación
    const handleLoginSuccess = async (credentialResponse) => {
        const token = credentialResponse.credential

        try {
            const response = await fetch(`${authURL}/login/google`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({token: token})
            })

            const data = await response.json()

            // Si la autenticación es exitosa, se almacena el token y la información del usuario en el localStorage
            if (data.success) {
                localStorage.setItem('token', data.token)
                localStorage.setItem('userInfo', JSON.stringify(data.user_info))
                navigate('/')
            } else {
                console.log('Login failed:', data.message)
            }
        } catch (error) {
            console.error('Error during login:', error)
        }
    }

    const handleLoginFailure = () => {
        console.log('Login failed.')
    }

    return (
        <GoogleOAuthProvider clientId="496696206304-fsqr77k8ao63rv6tuskh5lu4ph5p4fo3.apps.googleusercontent.com">
            <GoogleLogin
                onSuccess={handleLoginSuccess}
                onError={handleLoginFailure}
                render={(renderProps) => (
                    <Button
                        variant="contained"
                        color="primary"
                        startIcon={<GoogleIcon/>}
                        onClick={renderProps.onClick}
                        disabled={renderProps.disabled}
                        style={{textTransform: 'none'}}
                    >
                        Sign in with Google
                    </Button>
                )}
            />
        </GoogleOAuthProvider>
    )
}

export default GoogleButton