''' Contact class '''
import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from util.db_util import DBUtil
from util.utils import snake_case, load_json_schema


class Contacts():
    ''' Contact class '''

    def __init__(self):
        self.class_name = type(self).__name__  # Contact
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self, name=None, address=None, phoneNumber=None, isDeceased=None):
        ''' get all contacts '''
        self.logger.info('name=%s address=%s phoneNumber=%s isDeceased=%s', name, address, phoneNumber, isDeceased)
        self.logger.info(list(self.collection.find({})))
        
        # add query parameters for if they are passed
        query = {}
        if name:
            query['name'] = name  # query = {'name': 'Dean'}
            self.logger.info('name: %s', query)
        if address:
            query['address'] = address # query = {'name': 'Dean', 'address': '12345 street'}
            self.logger.info('address: %s', query)
        if phoneNumber:
            query['phoneNumber'] = phoneNumber
            self.logger.info('phoneNumber: %s', query)
        if isDeceased is not None:
            query['isDeceased'] = isDeceased # query = {'isDeceased': True}
            self.logger.info('isDeceased: %s', query)

        return {
            'result': list(self.collection.find(query, {'_id': 0}))
        }, 200

    def get_one(self, name):
        ''' get one contact '''
        result = self.collection.find_one({'name': name}, {'_id': 0})
        if result:
            return result, 200
        return {
            'message': f'{name} not found'
        }, 404

    def create_one(self, payload):
        ''' Create a Contact '''
        added_contact = self.collection.find_one(payload)
        if added_contact:
            return {'message' : f' {payload} already in contacts'}, 409
        self.collection.insert_one(payload)
        return {
            'message': f'Created Contact: {payload}',
            'name': f'{payload["name"]}',
            'address': f'{payload["address"]}',
            'phoneNumber': f'{payload["phoneNumber"]}',
        }, 201

    def update_one(self, name, payload):
        ''' update a contact by name '''
        result = self.collection.find_one({'name': name}, {'_id': 0})
        if result:
            self.collection.update_one({'name': name}, {'$set': payload})
            return {'message': f'Updated {name}'}, 200
        return {
            'message': f'{name} not found'
        }, 404
    
    def delete_one(self, name):
        ''' delete a contact by name '''
        result = self.collection.find_one({'name': name}, {'_id': 0})
        if result:
            self.collection.delete_one(result)
            return { 
                'message': f'{name}- deleted from db' 
            }, 200
        return {
            'message': f' {name} not found'
        }, 404

    def validate_schema(self, payload):
        ''' Validates application definition against schema '''
        schema = load_json_schema('contact-schema.json')

        try:
            validate(payload, schema)
        except ValidationError as v_err:
            self.logger.warning('Schema validation error: %s', v_err)
            return {
                'error': 'Failed schema validation',
                'message': v_err.message,
                'data': payload
            }, 422
        except Exception as ex: # pylint: disable=broad-except
            self.logger.error('Unknown schema validation error: %s', ex)
            return {'error': 'Unknown schema validation',
                    'message': ex,
                    'data': payload
                }, 400
        return {
            'message': 'Application definition passed schema validation'
        }, 200
      