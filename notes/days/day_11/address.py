''' Address class '''


class Address():
    ''' Address class '''

    def __init__(self,
                 name=None,
                 business_name=None,
                 phone=None,
                 street=None,  
                 city= None,
                 state=None,
                 zipcode=None):
        self.name = name
        self.business_name = name
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
    def set_street(self):

        self.street

    def get_street(self):
        return self.street
        
    def set_name(self):
        self.name

    def get_name(self):
        return self.name

    def display(self, indent=0):
        '''print out the address'''
        spaces =''
        if indent:
            spaces= ' ' * indent
        #print(f'{spaces}{self.business_name}')
        # print(f'{spaces}{self.name}')
        #print(f'{spaces}{self.phone}')
        print(f'{spaces}{self.street}')
        print(f'{spaces}{self.city}, {self.state} {self.zipcode} ')

    

    