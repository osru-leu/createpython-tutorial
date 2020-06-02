class Work():
    '''address class '''
    def __init__(self,
                street = 'UNDEFINED in work',
                city = 'UNDEFINED in work',
                state = 'UNDEFINED in work',
                zipcode = 'UNDEFINED in work'):
        
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