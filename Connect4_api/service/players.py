import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from util.db_util import DBUtil 
from util.utils import snake_case, load_json_schema

class Players():
    ''' Players class '''
    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
        

    def get_all(self, playerId=None, displayName=None):
        # self.logger.info('playerId=%s displayName=%s', playerId, displayName)
        # self.logger.info(list(self.collection.find({}))
            query = {}
            return {
            'result': list(self.collection.find(query, {'_id': 0}))
        }, 200

    def get_one(self, display_name):
        ''' get one player by display name'''
        result = self.collection.find_one({'displayName': display_name}, {'_id': 0})

        if result:
            return result, 200
        return {'message': f'{display_name} not found'}, 404

    def create_one(self, display_name, payload):
        ''' create a player '''
        display_name_check = self.collection.find({'displayName': display_name}, {'_id': 0})
        
        print(f'display_name_check: {display_name_check}')
        if display_name_check:
            return {
                'Message': f'This displayName already exists'
            }, 400 # or 412?
      
        resp, code = self.validate_schema(payload)
        if code!= 200:
            return resp, code
        result = list(self.collection.find(
            {'playerId': {'$ne': None}}, {'_id': 0, 'playerId': 1}
            ).sort('playerId', -1).limit(1))
        if result:
            next_player_id = int(result[0]['playerId']) + 1
        else:
            next_player_id = 0
        #sets playerId
        payload['playerId'] = next_player_id
        self.collection.insert_one(payload)
        return {
            'message': f'Created player: {payload}'
        }, 201

    def update_one(self, display_name, payload):
        ''' update a player by display name '''
        result = self.collection.find_one({'displayName': display_name}, {'_id': 0})
        if result:
            self.collection.update_one({'displayName': display_name}, {'$set': payload})
            return {'message': f'Updated {display_name} {payload}'}, 200
        return {
            'message': f'playerId {display_name} not found'
        }, 404

    def delete_one(self, display_name):
        ''' delete a player by display name '''
        result = self.collection.find_one({'displayName': display_name}, {'_id': 0})
        if result:
            self.collection.delete_one({'displayName': display_name})
            return{ 'message': f'deleted {display_name} successfully'}, 200
        return {
            'message': f'displayName {display_name} not found'
        }, 404
        
            
    def validate_schema(self, payload):
        '''validates schema application definition against schema '''
        schema = load_json_schema('players-schema.json')

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


    