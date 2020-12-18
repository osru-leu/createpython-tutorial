from flask import request
from flask_restx import Namespace, Resource, fields

from service.games import Games

NS = Namespace(
    'games',
    description='Aint talkin about monopoly'
)

GAME = NS.model(
    'Game', {
        'title': fields.String(
            required=True,
            description='Game Title',
            example='Doom'
        ),
        'genre': fields.String(
            required=True,
            description='Game Category',
            example='Hack and Slash'
        )
    }
)


@NS.route('')# add title here?
class GamesCollection(Resource):
    ''' Game Collection Methods '''

    def get(self):
        ''' Returns list of games '''
        return Games().get_all()
    @NS.expect(GAME)
    def post(self):
        ''' Creates a game '''
        return Games().create_one(request.get_json())
   
@NS.route('/<string:title>')
class Game(Resource):
    ''' Game Methods '''

    def get(self, title):
        ''' Returns a game title name '''
        return Games().get_one(title)

    def put(self, title):
        ''' Updates a game title name '''
        return Games().update_one(title, request.json)

    def delete(self, title):
        ''' Deletes a game by title '''
        return Games().delete_one(title)


    # def delete(self, title): 
    #     ''' Deletes a game by title name '''
    #     return Games().delete_many(title)
