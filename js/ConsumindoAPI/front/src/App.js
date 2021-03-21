import {useEffect, useState} from 'react';
import './App.css';
import axios from 'axios';

function App() {

  const [post,setPosts] = useState([]);
  useEffect(()=>{
    axios.get('http://127.0.0.1').then(function(res){
        setPosts(res.data);
    })
  },[]);     

  return (
    <div className="App">{
          post.map(function(val){
              return (
                <div className="Noticias">
                    <img src={val.image} />
                    <p className="conteudo">{val.conteudo}</p>                    
                </div>
              );
        }
    )};
    </div>
  );
}

export default App;
