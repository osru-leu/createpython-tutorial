''' Contacts Endpoint '''
from flask import request
from flask_restx import Namespace, Resource, fields, inputs, reqparse

from service.contact import Contacts

NS = Namespace(
    'Contacts',
    description='Operations related to contacts'
)


#localhost:5000/contacts?name=value1
GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    'name', required=False, default=None,
    help='Optionally filter by name')
GET_PARSER.add_argument(
    'address', required=False, default=None,
    help='Optionally filter by address')
GET_PARSER.add_argument(
    'phoneNumber', required=False, default=None,
    help='Optionally filter by phone number')
GET_PARSER.add_argument(
    'isDeceased', type=inputs.boolean, required=False,
    help='Optionally filter by persons whom are deceased'

)
CONTACT = NS.model(
    'Contact', {
        'name': fields.String(
            required=True,
            description='First and last name',
            example='Bob Smith',
            pattern='^[A-Z]{1}[a-z]+( )[A-Z]{1}[a-z]+$'
        ),
        'address': fields.String(
            required=True,
            description='Location of residence',
            example='1234 Peppergrove Paris, TX 77856'
        ),
        'phoneNumber': fields.String(
            required=True,
            description='Phone Number',
            example='123-456-7890',
            pattern='^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        'isDeceased': fields.Boolean(
            default=False,
            description='Is the contact deceased'
        )
    }
)

PUT_CONTACT = NS.model(
    'Contact', {
        'name': fields.String(
            required=True,
            description='First and last name',
            example='Bob Smith',
            pattern='^[A-Z]{1}[a-z]+( )[A-Z]{1}[a-z]+$'
        ),
        'address': fields.String(
            required=True,
            description='Location of residence',
            example='1234 Peppergrove Paris, TX 77856'
        ),
        'phoneNumber': fields.String(
            required=True,
            description='Phone Number',
            example='123-456-7890',
            pattern='^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        'isDeceased': fields.Boolean(
            default=False,
            description='Is the contact deceased'
        )
    }
)

@NS.route("")
class ContactsCollection(Resource):
    '''Contacts Collection methods '''

    @NS.doc(parser=GET_PARSER)
    def get(self):
        ''' Returns list of contacts '''
        args = GET_PARSER.parse_args()
        return Contacts().get_all(args['name'], args['address'], args['phoneNumber'], args['isDeceased'])

    @NS.expect(CONTACT, validate=True)
    def post(self):
        ''' Creates a contact '''
        return Contacts().create_one(request.get_json())

   

@NS.route('/<string:last_name>/<string:first_name>')
class Contact(Resource):
    ''' Contact methods '''

    def get(self, last_name, first_name):
        ''' Returns a contact '''
        return Contacts().get_one(first_name + ' ' + last_name)

    @NS.expect(PUT_CONTACT, validate=True)
    def put(self, name):
        ''' Updates a contact '''
        return Contacts().update_one(name, request.get_json())

    def delete(self, name):
        ''' Deletes a contact by name '''
        return Contacts().delete_one(name)
    




# 'name': fields.String(
#             required=True,
#             description='First and last name',
#             example='Bob Smith',
#             pattern='^[A-Z]{1}[a-z]+( )[A-Z]{1}[a-z]+$'

# CONTACT = NS.model(
#     'Contact', {
#         'firstName': fields.String(
#             required=True,
#             description='First Name',
#             example='Bob',
#             pattern='^[A-Z]{1}[a-z]+$' 
#         ),
#         'lastName': fields.String(
#             required=True,
#             description='Last Name',
#             example='Smith',
#             pattern='^[A-Z]{1}[a-z]+$' 
#         ),
#         'address': fields.String(
#             required=True,
#             description='Location of residence',
#             example='1234 Peppergrove Paris, TX 77856'
#         ),
#         'phoneNumber': fields.String(
#             required=True,
#             description='Phone Number',
#             example='123-456-7890',
#             pattern='^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
#         ),
#         'isDeceased': fields.Boolean(
#             default=False,
#             description='Is the contact deceased'
#         )
#     }
# )
''' -rewatch the session and apply it to your code
        -take notes
    -adjust the schema in contact
    -finish web spacer, tracer, pickerparter fucking a dude. get some sleep
    -finish galaga tut '''