import React from 'react'

const Country = (props) =>{

    return(
        <div>
                <img src={`https://www.countryflags.io/${props.stats.CountryCode}/flat/64.png`} alt={props.stats.Country}></img>
                {props.stats.Country}
            <div>
                <p>{`Ativos : ${props.stats.Active}`}</p>
                <p>{`Confirmados : ${props.stats.Confirmed}`}</p>
                <p>{`Mortos : ${props.stats.Deaths}`}</p>
                <p>{`Recuperados : ${props.stats.Recovered}`}</p>
            </div>
        </div>
    )
    
}


export default Country
