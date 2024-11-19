import { Box, CircularProgress, IconButton } from '@mui/material';
import React, { useEffect, useRef, useState } from 'react';
import PlayArrowRoundedIcon from '@mui/icons-material/PlayArrowRounded';
import PauseRoundedIcon from '@mui/icons-material/PauseRounded';
const Audio = ({doneIA, message}) => {
    const audioRef = useRef(null);
    const [isPLaying, setIsPlaying] = useState(false)
    const [superURL,setSuperURL] = useState('')
    const [isWaiting,setIsWaiting] = useState(false)
    const [firstTime,setFirstTime]=useState(true)
    const IAUrl = process.env.REACT_APP_VERCEL_IA
                ? `https://${process.env.REACT_APP_VERCEL_IA}`
                : 'http://127.0.0.1:2003'
    useEffect(()=>{
      //Quiere decir que ya termino de procesarse
      async function funcAsynx (){
        if(doneIA )
          {
            setFirstTime(false)
           await getAudio();
          }
      }
      funcAsynx()
      
    },[doneIA])

    const handlePlay = () => {
    if (audioRef.current) {
        audioRef.current.play();
    }
    };

    const handlePause = () => {
    if (audioRef.current) {
        audioRef.current.pause();
    }
    };
    const handleOnClick = ()=>{

        if(superURL)
        if(isPLaying){
            handlePause();
        }
        else{
            handlePlay()
        }
        setIsPlaying(!isPLaying)
            
    }
    const getAudio= async ()=>{
      setIsWaiting(true)
      const response = await fetch(`${IAUrl}/text_to_speech`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: message})
    })

    
    const audioBlob = await response.blob()
    const audioUrl = URL.createObjectURL(audioBlob);
    setSuperURL(audioUrl)
    setIsWaiting(false)
    
    }
    const showElement=()=>{
      if(isWaiting)
        {
          console.log("Gano circulo")
          return <CircularProgress size={30} sx={{color: (theme) => theme.palette.primary.main}}/>
        }
        else{
          console.log("Gano el pausa/play")
          return( 
            <IconButton onClick={handleOnClick}>
              {isPLaying? <PauseRoundedIcon/>  : <PlayArrowRoundedIcon/>}
            </IconButton>
            ) 
     
        }
      
    }
    const handleOnError = async ()=>{
      //La primera vez siempre marca error
     if(!firstTime){
      await getAudio()
     }
    }
    return (
    <Box style={{ textAlign: 'center' }}>
        <audio ref={audioRef} 
        src={superURL}
        onError={handleOnError} 
        />
        <Box>
          {showElement()}
        </Box>
    </Box>
    );
    };

export default Audio;
