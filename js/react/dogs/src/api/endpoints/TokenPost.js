import React from  'react'

const TokenPost = () => {
    const [username, setUsername] =  React.useState('');
    const [password, setPassword] =  React.useState('');
    const [token, setToken] =  React.useState('');
    
    function handlerSubmit(event){
        event.preventDefault();
        console.log({username, password})

        fetch('https://dogsapi.origamid.dev/json/jwt-auth/v1/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username,
                password
            }),
        }).then(response => {
            console.log(response);
            return response.json();
        }).then(json =>{
            console.log(json);
            setToken(json.token);
            return json;
        })
    }

    return ( 
        <form onSubmit={handlerSubmit}>
            <input placeholder="Usuario"  type="text"  value={username} onChange={ ({target}) => setUsername(target.value)} />
            <input placeholder="password"  type="text"  value={password} onChange={ ({target}) => setPassword(target.value)} />
            <button>Enviar</button>
            <p> {token}</p>
        </form>
    )
}


export default TokenPost; 
