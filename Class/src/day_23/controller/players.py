from flask import request
from flask_restx import Namespace, Resource, fields, inputs, reqparse

from service.players import Players

NS = Namespace(
    'players',
    description='player information in game'
)
#parser
GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    "state", choices=["OFFLINE", "IN_GAME", "IN_LOBBY"], required=False, default="OFFLINE",
    help="Optionally filter by players online"
)
PLAYER = NS.model(
    'User', {
        "emailAddress": fields.String(
            required=True,
            description="Email address for user varification",
            example="bob@gmail.com"
        ),
        'username': fields.String(
            required=True,
            description="Username",
            example='Bobsthedude1234'
        ),
        "password": fields.String(
            required=True,
            description="Player specific unique password",
            example="Password1234!- one lowercase letter, one uppercase, one digit, one symbol, 8>= length, no spaces.",
            pattern=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.*\s).{8,}$'
        ),
    
        "displayName": fields.String(
            required=True,
            description="Name chosen by player for other players to see",
            example="TicTacs4urmom",
            #pattern="import no profanity package"
        ),
        "level": fields.String(
            required=False,
            description="Tracks player advancement",
            example="BadAss"
            
        ),
        "cumulativeScore": fields.Integer(
            required=False,
            description="Score accumlated from games won",
            example=456,
            #pattern=REGEX
        ),
        "gameId": fields.String(
            required=False,
            description="Unique numerical identifier",
            #example=
        ),
        "avatar": fields.String(
            required=False,
            description="Player chosen image",
            example="http://www.bobsavatars.com/kikicat",
            #pattern=REGEX
        ),
        "state": fields.String(
            required=True,
            description="Shows if the player is online",
            example="OFFLINE",
            enum=["IN_LOBBY", "IN_GAME", "OFFLINE"]
        )
        
    }
)
PUT_PLAYER = NS.model(
    'User', {
        "emailAddress": fields.String(
            required=True,
            description="Email address for user varification",
            example="bob@gmail.com"
        ),
        'username': fields.String(
            required=True,
            description="Username",
            example='Bobsthedude1234'
        ),
        "password": fields.String(
            required=True,
            description="Player specific unique password",
            example="Password1234!- one lowercase letter, one uppercase, one digit, one symbol, 8>= length, no spaces.",
            pattern=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.*\s).{8,}$'
        ),
        "displayName": fields.String(
            required=True,
            description="Name chosen by player for other players to see",
            example="TicTacs4urmom",
            #pattern="import no profanity package"
        ),
        "level": fields.String(
            required=False,
            description="Tracks player advancement",
            example="BadAss"
            
        ),
        "cumulativeScore": fields.Integer(
            required=False,
            description="Score accumlated from games won",
            example=456,
            #pattern=REGEX
        ),
        "gameId": fields.String(
            required=False,
            description="Unique numerical identifier",
            #example=
        ),
        "avatar": fields.String(
            required=False,
            description="Player chosen image",
            example="http://www.bobsavatars.com/kikicat",
            #pattern=REGEX
        ),
        "state": fields.String(
            required=True,
            description="Shows if the player is online",
            example="OFFLINE",
            enum=["IN_LOBBY", "IN_GAME", "OFFLINE"]
        )
        
    }
)
@NS.route("")
class PlayersCollection(Resource):
    '''player collection methods '''
    @NS.doc(parser=GET_PARSER)
    def get(self):
        ''' returns a list of all players '''
        args = GET_PARSER.parse_args()
        print(f'args={args}')
        return Players().get_all(args['state'])
    

    @NS.expect(PLAYER, validate=True)
    def post(self):
        ''' adds a new player '''
        print(f'request={request.get_json()}')
        return Players().create_one(request.get_json()) 


@NS.route("/<string:username>")
class Player(Resource):
    ''' Game methods '''

    def get(self, username):
        ''' gets a player by username '''
        return Players().get_one(username)
    @NS.expect(PUT_PLAYER, validate=True)
    def put(self, username):
        ''' updates a player's username via old username'''
        return Players().update_one(username, request.json)

    def delete(self, username):
        ''' deletes a player by username '''
        return Players().delete_one(username)

@NS.route("/<string:username>/<string:password>")
class PlayerPassword(Resource):
    @NS.expect(PUT_PLAYER, validate=True)
    def put(self, username, password):
        ''' updates a player username and password ''' #do this separately?
        return Players().update_many(username, password, request.json)

@NS.route("/<string:username>/history")
class PlayerHistory(Resource):
    ''' player history methods '''
    def get(self, username):
        return Players().get_history(username)

    