from contact import Contact

class AddressBook():

    def __init__(self):
        self.contacts = []


    def add_contact(self, contact=Contact()):
        ''' add a new contact tot he addresss book'''
        # Make sure they passed a Contact class
        if not isinstance(contact, Contact):
            print('[ERROR] contact is not a Contact class')
            return
        ''' add the contacts to the lsit of conatacts '''
        self.contacts.append(contact)
      #MAYBE MAKE A list_contact to return none if the contact is empty. check past assignments for this we did this

    def delete_contact(self, name):
        ''' deletes contact by name '''
        if self.contacts == []:
            return print('Not listed in Contacts. -list- your contacts to see available contacts')

        else:
            contact = self.get_by_name(name)
            self.contacts.remove(contact)
        return 'Contact Deleted'
# Do a separate method for deleting address?
    def delete_contact_by_address(self, address):

        if self.contacts == []:
            return print('Not listed in Contacts. -list- your contacts to see available contacts')
        else:
            contact = self.get_home_address(address)
            self.contacts.remove(contact)
        return 'Contact deleted by address search'

    def get(self):
    #''' returns LIST of contacts '''
        return self.contacts

    def get_home_address(self, address):

        for contact in self.contacts:
            if contact.get_home_address(address) == contact:
                return contact
            else:
                return 'No Address found'
                
    def get_by_name(self, name):
        ''' return list of contacts '''
        for contact in self.contacts:
            if contact.get_name(name) == name:
                return contact
            else:
                return 'No Contact by that name'

    def display(self):
        ''' print contacts from address book '''
        for contact in self.contacts:
            contact.display()
            # if self.contacts == []:
            #     return '----No Contacts in Address book----'
            # else:
                # contact.display()