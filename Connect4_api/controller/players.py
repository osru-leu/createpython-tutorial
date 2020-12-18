from flask import request
from flask_restx import Namespace, Resource, fields, inputs, reqparse

from service.players import Players

NS = Namespace(
    'players',
    description='player information in games'
)
#parser args here

PLAYER = NS.model(
    'Player', {
        
        'displayName':fields.String(
            required=True,
            unique=True,
            description='Player name for in-game use',
            example='Connectf@rt',
            

        )
    }
)

PUT_PLAYER = NS.model(
    'Player', {
        
        'displayName':fields.String(
            required=True,
            unique=True,
            description='Player name for in-game use',
            example='Connectf@rt',
            

        )
    }
)
@NS.route("")
class PlayersCollection(Resource):
    ''' player collection methods '''
    def get(self):
        ''' returns a list of all players '''
        return Players().get_all()

    @NS.expect(PUT_PLAYER, validate=True)
    def post(self, display_name='displayName'):
        ''' adds a new player '''
        print(f'request={request.get_json()}')
        return Players().create_one(display_name, request.get_json())

@NS.route("/<string:display_name>")
class Player(Resource):
    ''' player methods '''

    def get(self, display_name):
        ''' get a player by display name'''
        return Players().get_one(display_name)

    def delete(self, display_name):
        ''' deletes a player by display name '''
        return Players().delete_one(display_name)

    @NS.expect(PUT_PLAYER, validate=True)
    def put(self, display_name):
        ''' updates a player by display name '''
        return Players().update_one(display_name, request.json)

    