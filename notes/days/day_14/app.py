""" Entry Point """
# from service.example import Example
from service.movie import Movie

import util.logging_setup

def get_movie_info():
    Movie (
    name = input('what is the name?'))
    return dict(Movie)

#         return dict(Movie(
#         name = input('What is the movie name?'),
#         starring = input('Starring who? '),
#         director = input('Who is the director? '),
#         category = input('What is the category? ')))
    #return Movie({'movieName': input('What is the Movie Name? ').lower().strip(' ')})

if __name__ == "__main__":
    
    while True:
        
        COMMAND = input('Would you like to -Add- -Find- or -Delete- a movie?' ).lower().strip(' ')
        if COMMAND == 'add':
            Movie().add_item(get_movie_info())
        elif COMMAND == 'find':
            '''testing find'''
            # ACTION = input('what is the name?')
            # MOVIE = Movie().find_one(ACTION)
            Movie().find_one(get_movie_info())
            
        # elif COMMAND == 'delete':
        #     Movie().delete_one(#get_movie_info())
        else:
            print(f'{COMMAND} is invalid')
   