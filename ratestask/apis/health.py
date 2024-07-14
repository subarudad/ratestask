from flask_restx import Namespace, Resource, fields


api = Namespace('health', description='healthcheck api')
health = api.model('Health', {
    'healthcheck': fields.String(required=True, description='The health status'),
    'status_code': fields.String(required=True, description='The status code'),
})


@api.route('')
@api.response(200, 'Success')
@api.response(400, 'Bad request')
@api.response(500, 'Internal server error')
class Health(Resource):
    @api.doc('get_health')
    @api.marshal_with(health)
    def get(self):
        response = {
            'healthcheck': "healthy",
            'status_code': 200
        }
        return response, 200

