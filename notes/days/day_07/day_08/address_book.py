'''ADDRESS BOOK CLASS ---2'''
from contact import Contact
class AddressBook():
    '''Address Book Class'''

    def __init__(self):
        self.contact = None

    def add_contact(self, contact=Contact()):
        '''Add a new contact to the address book '''
        # Make sure that they pased a Contact class
        if not isinstance(contact, Contact):
            print('[ERROR] contact is not Contact class')
            return

        # Add the contact to the list of contacts
        self.contact.append(contact.get())

        # self.contacts.append('-----------------------------------')
    # DO WE NEED TO DO AN add_work_contact() HERE? BECAUSE
    # WE ARE CALLING ADDRESSBOOK FROM app.py  

    def get(self):
        ''' Return list of contacts '''
        return self.contact