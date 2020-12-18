''' Games Endpoint '''
from flask import request
from flask_restx import Namespace, Resource, fields, inputs, reqparse

from service.games import Games

NS = Namespace(
    'games',
    description='game information fields'
)

GAME = NS.model(
    'Title', {
        'gameId': fields.String(
            required = True,
        ),
        'gameName': fields.String(
           required=True,
           description='Game title',
           example='Tic Tac Toe'
       ),
        'board': fields.String(
           required=True,
           description='List- space for game to take place',
           example= '0'     
        ),
        'status': fields.String(
            required=True,
            description='Current state or action in game',
            example='NOT_STARTED',
            enum=['NOT_STARTED', 'WIN', 'TIE', 'IN_ACTION', 
                'INVALID_MOVE', 'INVALID_PLAYER'],
        ),
        'playerUp': fields.String(
            required=True,
            description='Player turn notification',
            example='playerRed'
        ),
        'winner': fields.String(
            required=True,
            description='Game victor',
            example='Player 1 winner'
        ),
        'playerRed': fields.String(
            required=True,
            description='Player identifier in connect 4 game, 1 of 2',
            example='playerRed',
            pattern=r'^[0-2]$'
        ),
        'playerYellow': fields.String(
            required=True,
            description='Player identifier in connect 4 game, 1 of 2',
            example='playerYellow',
            pattern=r'^[0-2]$'
        )

    }
)

PUT_GAME = NS.model(
    'Title', {
        
        'gameName': fields.String(
           required=True,
           description='Game title',
           example='Tic Tac Toe'
       ),
        'board': fields.String(
           required=True,
           description='A list. Space for game to take place',
           example= '0,0,0,0'      
        ),
        'status': fields.String(
            required=True,
            description='Current state or action in game',
            example='NOT_STARTED',
            enum=['NOT_STARTED', 'WIN', 'TIE', 'IN_ACTION', 
                'INVALID_MOVE', 'INVALID_PLAYER'],
        ),
        'playerUp': fields.String(
            required=True,
            description='Player turn notification',
            example='playerRed'
        ),
        'winner': fields.String(
            required=True,
            description='Game victor',
            example='Player 1 winner'
        ),
        'playerRed': fields.String(
            required=True,
            description='Player identifier in connect 4 game, 1 of 2',
            example='1' ,
            pattern=r'^[0-2]$'
        ),
        'playerYellow': fields.String(
            required=True,
            description='Player identifier in connect 4 game, 1 of 2',
            example='2',
            pattern=r'^[0-2]$'
        )

    }
)
@NS.route("")
class GamesCollection(Resource):
    ''' games collection methods '''
    def get(self):
        ''' returns a list of all fields in games '''
        return Games().get_all()

    @NS.expect(GAME, validate=True)
    def post(self):
        ''' adds a new game '''
        print(f'request={request.get_json()}')
        return Games().create_one(request.get_json())

@NS.route("/<string:game_id>") 
class Game(Resource):
    ''' game methods '''

    def get(self, game_id):
        ''' gets a game by game Id '''
        return Games().get_one(game_id)
    @NS.expect(PUT_GAME, validate=True)
    def put(self, game_id):
        ''' updates a game by game Id '''
        print('putprint')
        return Games().update_one(game_id, request.json)

    def delete(self, game_id):
        ''' deletes a game by game Id '''
        return Games().delete_one(game_id)
