const connection = require('../database/connection')

module.exports = {
    async index(request, response){
        const incidents = await connection('incidents').select('*')
        
        return response.json(incidents)
    },

    async create(request, response){
        const { title, description, value} = request.body;
        const ong_id = request.headers.authorization;

        const [id] = await connection('incidents').insert({
            title,
            description,
            value,
            ong_id
        });
        return response.json({ id })
    },

    async delete(request, response){
        const { id } = request.params;
        const ong_id = request.headers.authorization;

        const incidents = await connection('incidents').where('id', id).select('ong_id').first();
        
        if (incidents.ong_id != ong_id){
            return response.status(401).json({error: 'Operation not Permitted'})
        }

        await connection('incidents').where('id', id).delete()
        return response.status(204).send()
    }
}