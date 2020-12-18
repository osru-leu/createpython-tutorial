''' sql test '''
import mysql.connector
from mysql.connector import errorcode


def get_database_cursor(cursor):

    try:
        conn = mysql.connector.connect(
            user='root', 
            password='Mysqlirka', 
            host='127.0.0.1',
            database='test')
        cursor = conn.cursor()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)

        return None
    # else:
    #     conn.commit()
    #     conn.close()
    

def create_user(first_name, last_name):
    ''''create user'''
    add_user = (
        'INSERT INTO users '
        '(firstName, lastName)'
        'VALUES (%s, %s)'
    )
    user_data = (first_name, last_name)   

    cursor.execute(add_user, user_data)


#def get_all_users():
    #'''get all users in database'''
get_database_cursor(create_user('Samuel', 'Urso'))
print('hello')