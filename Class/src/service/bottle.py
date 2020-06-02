""" Bottle class """
from service.item import Item


class Bottle(Item):
    ''' Bottle Class '''

    def __init__(self):
        super(Bottle, self).__init__()
        self.type = 'UNKNOWN'
        self.name = 'UNDEFINED'
        self.size = 'UNDEFINED'
        self.price = 'UNDEFINED'
        self.quantity = 'UNDEFINED'
    def get_bottle(self):
        ''' return the bottle info as a dictionary item '''
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price,
            'size': self.size,
            'quantity': self.quantity
        }

    def update_name(self, new_name):
        ''' Update a bottle name '''
        self.name = new_name

    def update_type(self, new_type):
        ''' Update a bottle type '''
        self.type = new_type.upper()

    def update_price(self, new_price):
        ''' Update a bottle price '''
        self.price = new_price

    def update_size(self, new_size):
        ''' Update a bottle size '''
        self.size = new_size

    def update_quantity(self, new_quantity):
        ''' Update a bottle quantity '''
        self.quantity = new_quantity