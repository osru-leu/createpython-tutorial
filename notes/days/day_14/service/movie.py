''' Contact class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Movie():
    ''' Contact class '''
#MIGHT HAVE TO MOVE THE CONSTRUCTORS TO A NEW py class
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

    # cd.collection.insert_one(item)
        
    def add_item(self, item):# how did we place the inputs here before?
        ''' Add an item to the database '''
        if self.find_one(query={ #just change the contents?
                'movieName': item['movieName']}):
            self.logger.error('Movie already exists for %s',
                              item['movieName'])
            return
        self.logger.info('Movie %s added successfully',
                         item['movieName'])
        self.collection.insert_one(item)

    def find_one(self, query):
        ''' find a item in collection '''
        return self.collection.find_one(filter=query)

    def find_many(self, query):
        ''' find a item in collection '''
        return self.collection.find(filter=query)

    def delete_one(self, query):
        ''' delete an item from collection '''
        return self.collection.delete_one(filter=query)

    def delete_many(self, query):
        ''' delete an item from collection '''
        return self.collection.delete_many(filter=query)

    def update(self, query, update_dict):
        ''' update a item in the collection '''
        result = self.collection.update_one(filter=query, update=update_dict)
        if result.modified_count == 0:
            self.logger.warning('Nothing changed')
        else:
            self.logger.info('New -> %s', self.find_one(query=query))

    
    ###################sets_and_gets##########################
    # def get(self):
    #     return {'movieName': self.name}
        #Movie({'movieName': input('What is the Movie Name? ').lower().strip(' ')})

    def get(self):
        ''' returns address '''
        return {
            'name': self.name,
            'starring': self.starring,
            'director': self.director,
            'category': self.category,
           
        }
   
    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name


    def set_director(self, director):
        self.director = director

    def get_director(self, director):
        return self.director
        

    def set_category(self, category):
        self.category = category

    def get_category(self, category):
        return self.category

