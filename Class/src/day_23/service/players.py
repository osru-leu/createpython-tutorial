import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from util.db_util import DBUtil
from util.utils import snake_case, load_json_schema

# MOVE PARSER TO GET_ONE FROM GET ALL. GET ALL SHOULD ONLY BE FOR EVERYTHING
#           -OR-
# DO ANOTHER GET_ALL BUT FOR THE SELECTION OF ONLINE OR OFFLINE PLAYERS? WHAT WOULD THIS BE USED FOR?
# IS IT NECESSARY?
class Players():
    '''Game class'''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self,
                emailAddress=None, 
                username=None, 
                password=None, 
                displayName=None,
                level=None,
                cumulativeScore=None,
                gameId=None, 
                avatar=None,
                state=None):

                #self.logger.info('emailAddress=%s username=%s password=%s displayName=%s', emailAddress, username, password, displayName)
                #self.logger.info(list(self.collection(find({})))
            query = {}
            return {
            'result': list(self.collection.find(query, {'_id': 0}))
        }, 200

    def get_one(self, username):
        ''' get one player profile by name '''
        result = self.collection.find_one({'username': username}, {'_id': 0})
        
        if result:
            return result, 200
        return {'message': f'{username} not found'}, 404

    def create_one(self, payload):
        ''' create a player '''
        user_found = self.collection.find_one({'username': payload["username"]}, {'_id': 0})
        if user_found:
            return {'message': f"{payload['username']} already exists"}
        resp, code = self.validate_schema(payload)
        if code != 200:
            return resp, code
        self.collection.insert_one(payload)
        return {'message': f'Created player: {payload}'
        }, 201

    def update_one(self, username, payload):
        ''' update a player by username '''
        result = self.collection.find_one({'username': username}, {'_id': 0})
        print('update_one1')
        if result:
            print(result)
            self.collection.update_one({"username": username}, {"$set": payload})
            return {'message':f'Updated {username}'}, 200
        return {
            'message': f'{username} not found'
        }, 404

    def update_many(self, username, password, payload):
        ''' update a player by username '''
        result = self.collection.find({'username': username}, {'password': password})

        if result:
            self.collection.update_many({"username": username}, {"$set": payload})
            return {'message':f'Updated {username}'}, 200
        return {
            'message': f'{username} not found'
        }, 404

    def delete_one(self, username):
        ''' deletes a player by username '''
        result = self.collection.find_one({"username": username}, {"_id": 0})
        print(result)
        print('here')
        if result:
            print('here2')
            self.collection.delete_one({'username': username}, {'_id': 0 })#PROBLEM LINE
            print('here3')
            return {'message': f'Deleted {username}'}, 200
        return {
            'message': f'{username} not found'
        }, 404

    def validate_schema(self, payload):
        ''' validates schema application definition against schema '''
        schema = load_json_schema('game-schema.json')

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

    def get_history(self, username):
       return self.collection_name.find({"username": username})
        