//import logo from './logo.svg';
import './App.css';
//import { NuevoComponente } from './components/NuevoComponente';
import { ComponenteDeChat } from './components/ComponenteDeChat';
import { Box } from '@mui/material';
//, Container
 
function App() {
  /*
  <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <NuevoComponente></NuevoComponente>
        <ComponenteDeChat/>
      </header>
    </div>
  */
  return (

    <Box sx = {{ bgcolor : '#343541', height: '110 vh',    padding: '20px'}}>
      
        <ComponenteDeChat/>
      
    </Box>
    
      );
}

export default App;
