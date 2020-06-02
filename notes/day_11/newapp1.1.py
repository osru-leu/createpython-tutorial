from address import Address 
from contact import Contact  
from address_book import AddressBook

def get_name_from_user():

    while True:
        name = input('What is the first and last name?: ').lower().split()
        if len(name) != 2:
            print('-First and Last name required-')
        else:
            break
    return (f'''First Name: {name[0].capitalize()}
Last Name: {name[1].capitalize()}''')


def get_phone_number_from_user():

    while True:
        ACTION = input('Would you like to add a phone number for this address (y/n)?: ').lower()
        if ACTION == 'y':
            
                phone = input('Phone Number: ').strip(' ')
                if not phone.isdigit():
                    print('-Must be all numbers-')
                elif len(phone) != int(10):
                    print('-Phone Number must be 10 digits-')
                else:
                    return (f'Phone: '+'{}-{}-{}'.format(phone[:3],phone[3:6],phone[6:10]))

        elif ACTION == 'n':
            return None
        else:
            print(f'{ACTION} is invalid')

    
def get_zip():

    while True:
        zipcode = input('Zipcode: ')
        if len(zipcode) != 5:
            print('-Zipcode must be 5 digits only-')
        elif not zipcode.isdigit():
            print('-Zipcode must consist of numbers only-')
        else:
            break
    return zipcode


def get_address_from_user():

     return Address(
        #name=get_name_from_user(),
        #phone=get_phone_number_from_user(),
        street=input('Street Address: ').capitalize(),
        city=input('City: ').capitalize(),
        state=input('State: ').upper(),
        zipcode=get_zip()
     )


def get_business_name():

    while True:
        ACTION = input('Would you like to add a business name (y/n)?').lower().strip(' ')
        if ACTION == 'y':
            bus_name = input('What is the name?: ')
            break
        elif ACTION == 'n':
            return None
        else:
            print(f'-{ACTION} is invalid-')
    return bus_name
        


def get_contact_from_user():
    ''' returns an Address class with datat entered from user '''
    contact = Contact(name=get_name_from_user())
    while True:
        ACTION = input('Would you like to enter a home address (y/n)?: ').lower()
        if ACTION == 'y':
            contact.set_home_address(get_address_from_user())
            contact.set_home_phone(get_phone_number_from_user())# make a new while loop? 
            break
        elif ACTION =='n':
            break
        else:
            print('Only "y" and "n" are valid commands')
            continue
    while True:
        SUB_ACTION = input('Would you like to enter a work address (y/n)?: ').lower() 
        if SUB_ACTION =='y':
            contact.set_business_name(get_business_name())
            contact.set_work_phone(get_phone_number_from_user())
            contact.set_work_address(get_address_from_user())
            break
        elif SUB_ACTION == 'n':
            break
        else:
            print('Only "y" and "n" are valid commands')
    return contact

def search_by_name():
    while True:
       
        name = input('What is the first and last name? ').lower().split()
        if len(name) != 2:
            print('-First and Last name required-')
        else:
            Contact.get_name(name)
        return name
        
       
#def search_by_address():     
# figure out the loop shit. make 2 if you have to? 
#figure out the for loop for the name only so you can get a return........im tired


ADDRESS_BOOK = AddressBook()
while True:
    ACTION = input('What would you like to do (list/search/add/edit/delete/exit?) \n').lower()
    if ACTION == 'add':
        ADDRESS_BOOK.add_contact(get_contact_from_user())
    elif ACTION == 'edit':
        print('Editing')
        #edit by..
    elif ACTION == 'list':
        ADDRESS_BOOK.display()    
        if ADDRESS_BOOK.contacts == []:
            print('You have 0 contacts...loser.')
         
    elif ACTION == 'search':
        SEARCH_ACT = input('Would you like to search by -Address- or by -Name-?').lower().strip(' ')
        if SEARCH_ACT == 'name':
            search_by_name()
        elif SEARCH_ACT == 'address':
            CONTACT = ADDRESS_BOOK.get_by_name(get_address_from_user())
            if CONTACT:
                CONTACT.display()
    
            
        
        
    elif ACTION == 'delete':
        # delete 'by' option?
        ADDRESS_BOOK.delete_contact(get_name_from_user())
        #ADDRESS_BOOK.delete_contact(get_address_from_user())
    elif ACTION == 'exit':
        print('Address Book Closed')
        break
    else:
        print(f'{ACTION} is invalid')