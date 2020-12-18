import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from util.db_util import DBUtil
from util.utils import snake_case, load_json_schema

class Games():
    ''' Games class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self,
                gameName=None,
                board=None,
                status=None,
                message=None,
                playerUp=None,
                playerRed=None,
                plyayerYellow=None):

                query = {}
                return {
                    'result': list(self.collection.find(query, {'_id': 0 }))
                }, 200

    def get_one(self, game_id):
        ''' get one game by game name '''
        result = self.collection.find_one({'gameId': int(game_id)}, {'_id': 0})

        if result: 
            return result, 200
        return {'message': f'gameId {game_id} not found'}, 404

    def create_one(self, payload):
        ''' create a game '''
        resp, code = self.validate_schema(payload)
        print('block 1')
        if code != 200:
            print('block 2')
            return resp, code
        #new game_id
        result = list(self.collection.find(
            {'gameId': {'$ne': None}}, {'_id': 0, 'gameId': 1}
            ).sort('gameId', -1).limit(1))
        if result:
            next_game_id = int(result[0]['gameId']) + 1
        else:
            next_game_id = 0
        # sets game_id
        payload['gameId'] = next_game_id
        self.collection.insert_one(payload)
        return {
            'message':f'Created game: {payload}'
        }, 201
    
    def delete_one(self, game_id):
        ''' delete a game by game name '''
        result = self.collection.find({'gameId': int(game_id)}, {'_id': 0})
        print(f'object{result}')
        print("deleteblock 1-----------------------------")
        if result:          #------------------------------------its not finding the result?
            print('deleteblock 2==========================')
            self.collection.delete_one({'gameId': int(game_id)})##PROBLEM
            print('deleteblock 3-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
            return {'message': f'Deleted game with gameId {game_id}'}, 200
        return {
            'messsage': f'{game_id} not found'
        }, 404

    def update_one(self, game_id, payload):
        ''' update a game by game_id '''
        print('update_one')
        result = self.collection.find({'gameId': int(game_id)}, {'_id': 0})# someting here not working
        print('update 1')
        if result:
            print('update 2')
            print('through name check')
            self.collection.update_one({'gameId': int(game_id)}, {"$set": payload})
            return {'message': f'Updated game with gameId {game_id}'}, 200
        return {
            'message': f'gameId {game_id} not found'
        }, 404

    def validate_schema(self, payload):
        ''' validates schema application definition against schema '''
        schema = load_json_schema('games-schema.json')

        try:
            validate(payload, schema)
        except ValidationError as v_err:
            self.logger.warning('Schema validation error: %s', v_err)
            return {
                'error': 'Failed schema validation',
                'message': v_err.message,
                'data': payload
            }, 422
        except Exception as ex:
            self.logger.error('Unknown schema validation error: %s', ex)
            return {
                'error': 'Failed schema validation',
                'message': ex,
                'data': payload
            }, 400
        return {
            'message': 'Application definition passed schema validation'
        }, 200
        
    





