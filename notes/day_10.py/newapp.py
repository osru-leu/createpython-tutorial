from address import Address
from contact import Contact



def get_name_from_user():

    while True:
        name = input('What is the first and last name?').split()
        if len(name) !=2:
            print('Must enter a first and last name.')
        else:
            break
    return (f'''First Name: {name[0].capitalize()} 
    Last Name: {name[1].capitalize()}''')

def get_work_address_from_user():

    return Address(
        name = input('What is the business name?').capitalize().strip(' '),
        phone = get_phone_number_from_user(),
        street=input('Street Address? ').capitalize(),
        city=input('City? ').upper(),
        state=input('State? ').upper(),
        zipcode=get_zip()
    )


def get_address_from_user():#import us addresses?
    ''' Returns a Address class with the data entered from user '''
    return Address(
        name = get_name_from_user(),
        street=input('Street Address? ').capitalize(),
        city=input('City? ').upper(), #import cities in funct?
        state=input('State? ').upper(),#import states
        zipcode=get_zip()
    )

def get_zip():
    
    while True:
        zipcode=input('Zipcode? ')
        if len(zipcode) != 5:
            print('Zipcode must be only 5 digits')
        elif not zipcode.isdigit():
            print('Zipcode must consist of numbers only.')
        else:
            break
    return zipcode


def get_phone_number_from_user():

    while True:
        if PHONE_ACTION == 'Y':
            phone = input('What is the phone number? \n').strip(' ')
            if not phone.isdigit():
                print('**!MUST BE IN A 10 DIGIT NUMBER FORMAT! NON DIGIT ENTRY!**')
            elif len(phone) != int(10):
                print('**!MUST BE IN A 10 DIGIT NUMBER FORMAT!**') 
            else:
                break
    return phone

HOME_ADDRESS = None
HOME_PHONE = '__________'
WORK_PHONE = '__________'
WORK_ADDRESS = None

print('-------Welcome to Python Addressbook-------\n')

while True:
    
    ACTION = input(f'''Would you like to add a:\n
    -HOME- address or -WORK- address
                   OR 
                 -NEXT- 
         for Phone Number entry
                   OR
                 -EXIT-?\n''').upper().strip(' ')
                 
    if ACTION == 'EXIT':

            EXIT_ACT = input('Are you sure YES/NO?\n ').upper()
            if EXIT_ACT == 'YES':
                print('-----Thank you for using Python Addressbook-----\n')
                exit()
            elif EXIT_ACT == 'NO':
                continue
            else:
                print(f'{EXIT_ACT} is invalid')
    
    if ACTION == 'HOME':
        HOME_ADDRESS = get_address_from_user()
        #donde append?                                 ARE HOME AND WORK REDUNDANT?
    elif ACTION == 'WORK':
        WORK_ADDRESS = get_work_address_from_user()
    elif ACTION == 'NEXT':
        pass
    else:
        print(f'\n{ACTION} is invalid. Please input a valid command')
        continue
####################################################################################
    while True:     # MAKE THIS INTO THE get_phone_number_from_user() funct? AND OR SOURCE IT FROM CLASS?
        PHONE_ACTION = input('Would you like to add a phone number (Y/N)?\n').upper().strip(' ')
        if PHONE_ACTION == 'Y':
            # PHONE_ACTION = get_phone_number_from_user()
            PHONE_SUB = input('Work or Home? ').upper()
            if PHONE_SUB == 'WORK':
                WORK_PHONE = get_phone_number_from_user()
            elif PHONE_SUB =='HOME':
                HOME_PHONE = get_phone_number_from_user()
            else:
                print('Invalid command')
                continue
        if PHONE_ACTION == 'N':
            break
    else:
        print('Action invalid. Please input a valid command\n')   
            
######################################################################################            
    while True:
        SUB_ACT = input('Would you like to -LIST- or -ADD- another address or -BACK- to main menu?\n').upper().strip(' ')
        if SUB_ACT == 'ADD':
            break
        
        elif SUB_ACT == 'LIST':
            print('YO CONTACT MESS')
            print('---------------------------------------')
            # print(f'First Name: {NAME[0].capitalize()}')
            # print(f'Last Name: {NAME[1].capitalize()}')
            # print('---------------------------------------')
            
            if HOME_ADDRESS:
                print('Home Address: ') 
                HOME_ADDRESS.display(4)
                HOME_ADDRESS.get()
                

            else:
                print('Home Address: __________')

            if HOME_PHONE:
                print(f'Home Phone: '+'{}-{}-{}'.format(HOME_PHONE[:3],HOME_PHONE[3:6],HOME_PHONE[6:10])+'\n')
            else:
                HOME_PHONE = HOME_PHONE
                print('---------------------------------------')

            if WORK_ADDRESS:
                print('Work Address:')
                WORK_ADDRESS.display(4)
            else: 
                print('Work Address: __________')

            if WORK_PHONE:
                print(f'Work Phone: '+'{}-{}-{}'.format(WORK_PHONE[:3],WORK_PHONE[3:6],WORK_PHONE[6:10])+'\n')
            else:
                WORK_PHONE = WORK_PHONE

        elif SUB_ACT not in ['ADD', 'LIST', 'BACK']:
            print(f'{SUB_ACT} invalid.')

        elif SUB_ACT == 'BACK':
            break
