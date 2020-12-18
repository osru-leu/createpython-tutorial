''' Games Class '''

class Games():
    ''' Games Class '''

    def get_all(self):
        ''' Get all movies '''
        return {
            'games':[
                {'gameTitle': 'game1',
                    'gameGenre': 'genre1'},
                {'gameTitle': 'game2',
                    'gameGenre': 'genre2'},
            ]
        }, 200

    def get_one(self, title):
        ''' Get one game by title '''
        return {
            'message': f'Found game {title}'
        }, 200

    def create_one(self, payload):
        ''' Create a game '''
        return {
            'message': f'Created game: {payload}',
            'gameTitle': f'{payload["title"]}',
            'gameGenre': f'{payload["genre"]}',
        }, 201

    def update_one(self, title, payload):
        ''' update one game by title '''
        return {'message': f'Update {title}'}, 200

    def delete_one(self, title):
        ''' delete one movie by title '''
        return{'message': f'Delete {title}'}, 200

    def delete_many(self, title):
        return{'message': f'Delete {title}'}, 200

