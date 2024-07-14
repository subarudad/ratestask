from flask_restx import Namespace, Resource, fields, inputs
from ratestask.utils import get_average_prices


api = Namespace('rates', description='Rates api')
average_price = api.model('Average price', {
    'day': fields.String(required=True, description='date'),
    'average_price': fields.Float(required=True, description='average price'),
})

parser = api.parser()
parser.add_argument('date_from', type=inputs.date, required=True, location='args')
parser.add_argument('date_to', type=inputs.date, required=True, location='args')
parser.add_argument('origin', required=True, location='args')
parser.add_argument('destination', required=True, location='args')


@api.route('')
class AveragePrices(Resource):
    @api.doc(params={
        'date_from': {'description': 'query from this date', 'type': 'date', 'default': '2016-01-01'},
        'date_to': {'description': 'query to this date', 'type': 'date', 'default': '2016-01-10'},
        'origin': {'description': 'origin of shipment', 'type': 'string', 'default': 'CNSGH'},
        'destination': {'description': 'destination of shipment', 'type': 'string', 'default': 'north_europe_main'}
    })
    @api.marshal_list_with(average_price)
    def get(self):
        req_args = parser.parse_args()
        date_from = req_args['date_from']
        date_to = req_args['date_to']
        origin = req_args['origin']
        destination = req_args['destination']

        prices = get_average_prices(date_from, date_to, origin, destination)
        return prices

