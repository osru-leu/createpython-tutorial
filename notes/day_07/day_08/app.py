''' Main entrypoint----1'''
from address import Address
from address_book import AddressBook
from contact import Contact
from work import Work
from work_address import WorkAddress
from workcontact import WorkContact

if __name__ == "__main__":
    
    while True:
        ''' START WITH INPUT '''
        COMMAND = input('What would you like to do (add, list, exit)? ').lower()
        if COMMAND == 'exit':
            print('Deuce deuce!')
            break
        elif COMMAND == 'add':
            ADDRESS_BOOK = AddressBook()
            WORK_ADDRESS = WorkAddress()
        
            PER_NAME = input('What is your name?').upper()
            PER_PHONE = input('Phone: ')
            ADDRESS_BOOK.add_contact(
            Contact(
                name = PER_NAME,
                phone= PER_PHONE,
                home_address=Address(
                    street= input('Street number and street: '),
                    city=input('City: ').upper(),
                    state=input('State: ').upper(),
                    zipcode=input('Zipcode: '))
                )
            )   
            while True:
                SUB_COMND = input('would you like to add your work information yes or no? ').upper()
                if SUB_COMND == 'NO':
                    break
                elif SUB_COMND == 'YES':
                    co_name = input('What is the company name?').lower()

                    co_phone = input('What is the company phone number? ')

                    WORK_ADDRESS.add_contact(
                        WorkContact( 
                    work_name = co_name,
                    work_phone= co_phone,
                    work_address=Work(
                        street= input('Street number and street: '),
                        city=input('City: ').upper(),
                        state=input('State: ').upper(),
                        zipcode=input('Zipcode: '))
                        
                    )
                )   
                    
                else:
                    print(f'{SUB_COMND} is not valid.')
                    continue
        elif COMMAND == 'list':
            print(ADDRESS_BOOK.get())
            print(WORK_ADDRESS.get())
        else:
            print(f'Man you know {COMMAND} aint what I asked you.')
