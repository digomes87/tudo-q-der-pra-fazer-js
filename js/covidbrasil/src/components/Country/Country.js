import React from 'react'

const Country = (props) =>{

    return(
        <div>
            <h1>
                <img src={`https://www.countryflags.io/${props.stats.CountryCode}/flat/64.png`} />
                {props.stats.Country}
            </h1>
        </div>
    )
    
}


export default Country
