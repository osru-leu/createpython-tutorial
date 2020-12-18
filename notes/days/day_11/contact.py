from address import Address

class Contact():
    ''' Contact class '''

    def __init__(self,
                 name=None,
                 home_phone=None,
                 home_address=None,
                 business_name =None,   #FIGURE OUT HOW TO MAKE THIS COMEBACK AS NOTHING/BLANK
                 work_phone=None,
                 work_address=None):

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
        self.home_phone = home_phone
        self.home_address = home_address
        self.business_name = business_name
        self.work_address = work_address
        self.work_phone= work_phone

    def get(self):
        ''' Return contact '''
        contact = {
            'name': self.name,
            'home_phone': self.home_phone,
            'business_name':self.business_name,
            'work_phone': self.work_phone
        }
        if self.home_address:
            contact['home_address'] = self.home_address.get()
        if self.work_address:
            contact['work_address'] = self.work_address.get()
        return contact


    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        ''' return contact name '''
        return self.name


    def set_home_address(self, address):
        ''' set the home address for the contact '''
        self.home_address = address

    def get_home_address(self, address):
        return self.home_address       

    def set_work_address(self, address):
        ''' set the work address for the contact '''
        self.work_address = address


    def set_business_name(self, name):
        self.business_name = name
    
    def get_business_name(self):
        return self.business_name
    
   

    def set_home_phone(self, home_phone):
        self.home_phone = home_phone

    def get_home_phone(self):
        return self.home_phone


    def set_work_phone(self, work_phone):
        self.work_phone = work_phone
    
    def get_work_phone(self):
        return self.work_phone

        
    def display(self):
        ''' Print out contact'''
        print(f'{self.name}')
        if self.home_address:       # DO WE WANT TO if else if else each category here?
            print('Home Address:')
            self.home_address.display(indent=4)
            print(f'Home Phone: {self.home_phone}')
            print(f'Business Name: {self.business_name}')
            print(f'Work Phone: {self.work_phone}')
        else:
            print('Home Address:__________')
        if self.work_address:
            print('Work Address:')
            self.work_address.display(indent=4)
        else:
            print('Work Address:__________')
        # else:
        #     return None
            #print('')

        # else:
        #     return print('You have 0 contacts')

        # if self.home_phone:         #leave this to see what happens
        #     print('Home Phone: ')   # might cause probs definite repeat
        #     self.home_phone.display(indent=2)
       
        # if self.work_phone:
        #     print('Work Phone: ')
        #     self.work_phone.display(indent=2)
       
        # if self.business_name:
        #     print('Business Name:') 
        #     self.business_name.display(indent=4)
        
       