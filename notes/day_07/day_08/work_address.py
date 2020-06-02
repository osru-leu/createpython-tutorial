# '''Work Address class'''
from workcontact import WorkContact
class WorkAddress():
   
    def __init__(self):
        self.workcontact = None

    def add_contact(self, workcontact=WorkContact()):

        '''Add a new contact to the address book '''
        # Make sure that they pased a Contact class
        if not isinstance(workcontact, WorkContact):
            print('[ERROR] contact is not Contact class')
            return
         # Add the contact to the list of contacts
        self.workcontact.append(workcontact.get())


    def get(self):
        ''' Return list of contacts '''
        return self.workcontact