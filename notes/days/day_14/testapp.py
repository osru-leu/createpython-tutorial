from service.movie import Movie
import util.logging_setup


if __name__ == "__main__":
    

        Movie().add_item(
        {
            'movieName': 'LoggJammin',
            'director': 'Jackie Treehorn',
            'starring': 'Carl Hungus',
            'Category': 'Adult',
        }
    )


        MOVIE = Movie().find_one({'movieName': 'LoggJammin'})
        print(MOVIE)
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