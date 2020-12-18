""" Entry Point """
# from service.example import Example
from service.movie import Movie

import util.logging_setup


def get_movie_info():

    return Movie(
        name = input('What is the Movie Name? ').lower().strip(' '),
        starring = input('Starring who? '),
        director = input('Who is the director? '),
        category = input('What is the category? '),


    )
if __name__ == "__main__":
    
    while True:
        
        COMMAND = input('Would you like to -Add- -Find- or -Delete- a movie?' ).lower().strip(' ')
        if COMMAND == 'add':
            Movie().add_item(get_movie_info())
        {
            'movieName': 'LoggJammin',
            'director': 'Jackie Treehorn',
            'starring': 'Carl Hungus',
            'Category': 'Adult',
        }
    ))
    # Movie().add_item(
    #     {
    #         'firstName': 'Dean',
    #         'lastName': 'Chin',
    #         'address': '909 Golden Palomino Court',
    #         'city': 'Austin',
    #         'state': 'TX',
    #         'zipcode': '78732'
    #     }
    # )
   

    # # print('--- ONE ----')
    # CONTACT = Contact().find_many({'lastName': 'Chin'})
    # print(list(CONTACT))
    # # Contact().delete_one({'lastName': 'Chin'})
    # Contact().delete_many({'lastName': 'Chin'})
    # # print('--- TWO ----')
    # CONTACT = Contact().find_many({'lastName': 'Chin'})
    # print(list(CONTACT))
    # Contact().update(query={'firstName': 'Mrs', 'lastName': 'Jackson'},
    #                  update_dict={'$set': {'address': '123 Wheels of Steel'}})
    MOVIE = Movie()