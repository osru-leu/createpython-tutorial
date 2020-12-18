import logging

from util.db_util import DBUtil
from util.utils import snake_case




class Movie():
#REMEMBER YOU WILL NEED TO ADD THE UTIL AND THE INITS
    def __init__(self,
                 name=None,
                 director=None,
                 starring=None,
                 category=None):

        self.class_name = type(self).__name__ 
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
        
        self.name = name
        self.director = director
        self.starring = starring
        self.category = category

    def add_item(self, item):

        if self.find_one(query={
            'movie': item['movieName']}):
            self.logger.error('Movie already exists for %s',
                                item['movie'])
            return
        self.logger.info('Movie %s succesfully added',
                            item['movie'])
        self.collection.insert_one(item)


    def find_one(self, query):
        return self.collection.find_one(filter=query)




    