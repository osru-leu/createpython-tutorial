''' Address class '''


class Address():
    ''' Address class '''

    def __init__(self,
                 name=None,
                 phone=None,
                 street=None,  
                 city= None,
                 state=None,
                 zipcode=None):
        self.name = name
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get(self):
        ''' returns address '''
        return {
            'name': self.name,
            'phone': self.phone,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode
        }
    def get_street(self):
        '''set street address'''
        return self.street

    def set_street(self, street):
        '''set street addresss'''
        self.street = street
        
    def display(self, indent=0):
        '''print out the address'''
        spaces =''
        if indent:
            spaces= ' ' * indent
        print(f'{spaces}{self.name}')
        print(f'{spaces}{self.phone}')
        print(f'{spaces}{self.street}')
        print(f'{spaces}{self.city}, {self.state} {self.zipcode} ')

    