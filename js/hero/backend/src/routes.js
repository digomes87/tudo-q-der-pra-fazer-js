const express =  require('express')

const routes = express.Router();

routes.post('/users', (request, response) =>{
    const params =  request.body;

    console.log(params)

    return response.json({
        nome: 'Semana Medway',
        idade: 34
    });
});


module.exports = routes;