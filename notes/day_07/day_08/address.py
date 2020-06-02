'''Address Class'''
'''STARTING POINT BUT WE ARE WORKING IT BACKWARDS --4'''

class Address():
    def __init__(self,
                street = 'UNDEFINED in Address',
                city = 'UNDEFINED in Address',
                state = 'UNDEFINED in Address',
                zipcode = 'UNDEFINED in Address'):
        
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get(self):
        
        return {
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode
        }