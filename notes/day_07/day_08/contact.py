''' Contact class '''
from address import Address


class Contact():
    ''' Contact class '''

    def __init__(self,
                 name='UNDEFINED',
                 phone='UNDEFINED',
                 home_address=Address()):
                #  work_address=Address()):

        # Check if home address is a valid address
        if not isinstance(home_address, Address):
            print('[ERROR] home_address is not a Address class')
            return

        # Check if work address is a valid address
        # if not isinstance(work_address, Address):
        #     print('[ERROR] work_address is not a Address class')
        #     return

        # Set class variables
        self.name = name
        self.phone = phone
        self.home_address = home_address
        # self.work_address = work_address

    def get(self):
        ''' Return contact '''
        return {
            'name': self.name,
            'phone': self.phone,
            'home_address': self.home_address.get()
            # 'work_address': self.work_address.get()
        }