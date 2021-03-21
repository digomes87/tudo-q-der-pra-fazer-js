import React from 'react';
import './App.css';

class App extends React.Component{
    constructor(){
        super();
        this.state = {
            name: 'Diego',
        }
    }
   render(){
    return(
        this.state.name
    )
   }
}
export default App;
