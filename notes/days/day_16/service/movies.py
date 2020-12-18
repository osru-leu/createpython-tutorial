'''Movies Class '''

class Movies():
    ''' Movies Class '''

    def get_all(self):
        ''' get all movies '''
        return{
            'movies': [
                {'title': 'movie1'},
                {'title': 'movie2'},
            ]
        }, 200

    def get_one(self, title):
        ''' get one movie by title '''
        return {
            'message': f'Found movie {title}'
        }, 200

    def create_one(self, payload):
        ''' Create a movie '''
        return {
            'message': f'Created movie: {payload}',
            'movieName': f'{payload["title"]}',
            'movieGenre': f'{payload["genre"]}',
        }, 201

    def update_one(self, title, payload):
        ''' update one movie by title '''
        return {'messsage': f'Update {title}'}, 200

    def delete_one(self, title):
        ''' delete one movie by title '''
        return{'message': f'Delete {title}'}, 200

    