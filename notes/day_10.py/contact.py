from address import Address

class Contact():
    ''' Contact class '''

    def __init__(self,
                 name= None,
                 phone= None,
                 home_address=Address(),
                 work_address=Address()):

        # Check if home address is a valid address
        if home_address and not isinstance(home_address, Address):
            print('[ERROR] home_address is not a Address class')
            
            return

        # Check if work address is a valid address
        if work_address and not isinstance(work_address, Address):
            print('[ERROR] work_address is not a Address class')

            return
    
        # Set class variables
        self.name = name
        self.phone = phone
        self.home_address = home_address
        self.work_address = work_address

    def get(self):
        ''' Return contact '''
        contact = {
            'name': self.name,
            'phone': self.phone
        }
        if self.home_address:
            contact['home_address'] = self.home_address.get()
        if self.work_address:
            contact['work_address'] = self.work_address.get()
        return contact
        
    def display(self):
        ''' Print out contact'''
        print(f'Name: {self.name}')
        print(f'Phone: {self.phone}')
        if self.phone:
            print('Phone:')
            self.phone.display(indent=2)
        if self.home_address:
            print('Home Address:')
            self.home_address.display(indent=4)
        if self.work_address:
            print('Work Address:')
            self.work_address.display(indent=4)
        print('')
       