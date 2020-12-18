"""
Handles all database interactions
"""
from pymongo import MongoClient

import settings

class DBUtil:

    '''handles data base interations'''

    db_host = settings.DB_HOST
    db_user = settings.DB_USER
    db_password = settings.DB_PASSWORD
    db_port = settings.DB_PORT
    db_auth_mech = 'SCRAM-SHA-1'


    def __init__(self, db_name='movies'):
        self.client = MongoClient(
            self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_password,
            authMechanism=self.db_auth_mech
        )
        self.db_client = self.client[db_name]

    def get_db(self):
        '''returns database client'''
        return self.db_client

    def get_collection(self, collection_name):
        '''returns a collection from db '''
        return self.db_client[collection_name]

    def query(self, collection_name, query=None, fields=None):
        '''query data in collection'''
        query = query if query else {}
        items = list(
            self.get_collection(
                collection_name
            ).find(query, fields))
        return {
            'items':items
        },200

    def close_db_connection(self):
        ''' terminate database connect '''
        return self.client.close()