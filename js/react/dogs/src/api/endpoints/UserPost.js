import React from  'react'

const UserPost = () => {
    const [username, setUsername] =  React.useState('');
    const [email, setEmail] =  React.useState('');
    const [password, setPassword] =  React.useState('');
    
    function handlerSubmit(event){
        event.preventDefault();
        console.log({username, email, password})

        fetch('https://dogsapi.origamid.dev/json/api/user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username,
                email,
                password
            }),
        }).then(response => {
            console.log(response);
            return response.json();
        }).then(json =>{
            console.log(json);
            return json;
        })
    }

    return ( 
        <form onSubmit={handlerSubmit}>
            <input placeholder="Usuario"  type="text"  value={username} onChange={ ({target}) => setUsername(target.value)} />
            <input placeholder="email"  type="text"  value={email} onChange={ ({target}) => setEmail(target.value)} />
            <input placeholder="password"  type="text"  value={password} onChange={ ({target}) => setPassword(target.value)} />
            <button>Enviar</button>
        </form>
    )
}


export default UserPost;    
