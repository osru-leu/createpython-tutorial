''' Games Class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case



class Games():
    ''' Games Class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self):
        ''' Get all movies '''
        self.logger.info(list(self.collection.find({})))
        return {
            'result': list(self.collection.find({}, {'_id': 0}))
        }, 200
        # return {
        #     'games':[
        #         {'gameTitle': 'game1',
        #             'gameGenre': 'genre1'},
        #         {'gameTitle': 'game2',
        #             'gameGenre': 'genre2'},
        #     ]
        # }, 200

    def get_one(self, title):
        ''' Get one game by title '''
        result = self.collection.find_one({'title': title}, {'_id': 0})
        if result:
            return result, 200
        return {
            'message': f' {title} not found'
        }, 404

    def create_one(self, payload):
        ''' Create a game '''
        added_title = self.collection.find_one(payload)
        if added_title:
            return {'message': f'Duplicate Error {payload} already in database'}
        self.collection.insert_one(payload)
        return {
            'message': f'Created game: {payload}',
            'gameTitle': f'{payload["title"]}',
            'gameGenre': f'{payload["genre"]}',
        }, 201

    def update_one(self, title, payload):
        ''' update one game by title '''
        result = self.collection.find_one({'title': title}, {'_id': 0})
        if result:
            self.collection.update_one({'title': title}, {'_id': 0})
            return {'message': f'Updated {title}'}, 200
        return {
            'message': f'{title} not found'
        }, 404

    def delete_one(self, title):
        ''' delete one game by title '''
        result = self.collection.find_one({'title': title}, {'_id': 0})
        if result:
            self.collection.delete_one(result)
            return {
                'message': f'{title} successfully deleted from db'
            }, 200
        return {
            'message': f'{title} not found'}, 404

    # def delete_many(self, title): 
    #     ''' delete multiple games of the same title by title '''
    #     # result = self.collection.find({'title': title}, {'_id': 0}) #NO '_d'?  use get_all logger? find_many? or get_all
    #     result = self.collection.find({'title': title}, {'_id': 0})
        
    #     if result:
    #         self.collection.delete_many(result)
    #         return {
    #             'message': f'All titles by {title} have been deleted'
    #         }, 200
    #     return {
    #         f'{title} not found'}, 404
