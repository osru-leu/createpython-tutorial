(''' app functions ''')
from address import Address
from contact import Contact

# Scenario One:
# Regular Contact with an option for adding in work information.
# Name:
# Phone Number:
# Home Address:
# No work Address

# Prompting the user for information:
# Always get name?
# Ask if they want to put in home information?
# Ask if they want to put in work information?

# Dean Chin
# 123-456-7890
# 111 street
# Austin, TX 78732

#  Get full name
# while True:
#     FULL_NAME = input('What is your first name and last name? ').split()
#     if len(FULL_NAME) != 2:
#         print(
#             '[ERROR] Must enter your first and last name seperated by a space')
#     else:
#         break

# if input('Do you want to enter your home address (Y/N)? ').upper() == 'Y':
#     HOME_STREET = input('What is your home street name? ')
#     HOME_CITY = input('What is your home city? ')
#     HOME_STATE = input('What is your home state? ')
#     HOME_ZIP = input('What is your home zip? ')
#     HOME_ADDRESS = Address(
#         street=HOME_STREET,
#         city=HOME_CITY,
#         state=HOME_STATE,
#         zipcode=HOME_ZIP
    # )

#  Get full name
# while True:
#     FULL_NAME = input('What is your first name and last name? ').split()
#     if len(FULL_NAME) != 2:
#         print(
#             '[ERROR] Must enter your first and last name seperated by a space')
#     else:
#         break

def get_name_from_user():
    ''' get name from user '''
    while True:
        name = input('What is your first name and last name? ').upper().split()
        if len(name) != 2:
            print(
                '[ERROR] Must enter your first and last name seperated by a space')
        else:
            break
    return name

def get_address_from_user():
    ''' Returns a Address class with the data entered from user '''
    return Address(
        street=input('Street Address? '),
        city=input('City? ').upper(),
        state=input('State? ').upper(),
        zipcode=input('Zipcode? ')
    )
    
def get_phone_number_from_user():

    while True:
        if HOME_PHONE == 'Y':
            phone = input('What is the phone number? ')
            if not phone.isdigit():
                print('**!MUST BE IN A 10 DIGIT NUMBER FORMAT! NON DIGIT ENTRY!**')
            elif len(phone) < int(10):
                print('**!MUST BE IN A 10 DIGIT NUMBER FORMAT!**') 
            else:
                break
    return phone
    #.format(phone[:3],phone[3:6],phone[6:10])  # all the buitl in functions ADD A PHONE.PY THEN TRY ANOTHER METHOD?
    
    # ''' check for proper number of digits'''
    # ''' check for isdigit'''
    # ''' reformat input to output: (_ _ _)-_ _ _-_ _ _ _ , refer back to first assignment '''

def loop_check(command):

    if command not in 'Y' or 'N':
        print("Only 'Y' or 'N' are valid commands ")
    return command
    

# NO_ENTRY = 'NO ENTRY' 
HOME_ADDRESS = 'NO ENTRY' 
HOME_PHONE = 'NO ENTRY'
WORK_ADDRESS = None
WORK_PHONE = None

'''' START HERE. IF YOU NEED TO TRACE YOUR STEPS REFORMAT HOME_PHONE TO THE SAME AS WORK_PHONE PROBABLY HAVE TOO MANY LOOPS'''
# HOME_PHONE  = input('Would you like to add a home phone number(Y/N) ').upper().strip(' ')                                          
# HOME_PHONE = get_phone_number_from_user()
        
# MAIN ENTRY HERE? 
# MAIN AND OR THE WHILE LOOP HERE
NAME = get_name_from_user()
while True:
    HOME_ADDRESS = input('Do you want to enter your home address (Y/N)? ').upper().strip(' ') 
    if HOME_ADDRESS == 'Y':
        HOME_ADDRESS = get_address_from_user()
        break
    elif HOME_ADDRESS =='N':
        break
    else:
        HOME_ADDRESS = loop_check(HOME_ADDRESS)
        

if input('Would you like to add a home phone number(Y/N) ').upper().strip(' ') == HOME_PHONE:                                           
    HOME_PHONE = get_phone_number_from_user()
        
        
        

while True:
    WORK_ADDRESS = input('Do you want to enter your work address (Y/N)? ').upper().strip(' ')
    if WORK_ADDRESS == 'Y':
        WORK_ADDRESS = get_address_from_user()
    elif WORK_ADDRESS == 'N':
        break
    else:
        WORK_ADDRESS = loop_check(WORK_ADDRESS)
        
while True:
    if input('Would you like to add a work phone number (Y/N)? ').upper().strip(' ') == 'Y':
        WORK_PHONE = get_phone_number_from_user()
        break
    


print('-------------------------')
print('CONTACT INFO')
print('-------------------------')
print(f'First Name: {NAME[0].upper(),NAME[1:].lower()}')
print(f'Last Name: {NAME[1]}')

if HOME_ADDRESS:
    HOME_ADDRESS.display(4)
#     print(f'Home Address: {HOME_ADDRESS.get()}')
else:
    HOME_ADDRESS = HOME_ADDRESS
    print(HOME_ADDRESS)
    
if HOME_PHONE:
    print(f'Home Phone: ' +'{}-{}-{}'.format(HOME_PHONE[:3],HOME_PHONE[3:6],HOME_PHONE[6:10]))
else:
    HOME_PHONE = HOME_PHONE
    print(HOME_PHONE)

if WORK_ADDRESS:
    WORK_ADDRESS.display(4)
    # print(f'Work Address: {WORK_ADDRESS.get()}')
else:
    WORK_ADDRESS = WORK_ADDRESS
    print(WORK_ADDRESS)

if WORK_PHONE:
    print(f'Work Phone: '+'{}-{}-{}'.format(WORK_PHONE[:3],WORK_PHONE[3:6],WORK_PHONE[6:10]))
else:
    WORK_PHONE = WORK_PHONE
    print(WORK_PHONE)
# CONTACT = Contact(
#     name=FULL_NAME,
#     phone=HOME_PHONE,
#     home_address=HOME_ADDRESS,
#     work_address=WORK_ADDRESS

# )
#print(CONTACT.get())
print('-----------------')
#NAME.display(2)
#HOME_PHONE.display(3)
#HOME_ADDRESS.display(4)
print('-----------------')
#WORK_PHONE.display(4)
#WORK_ADDRESS.display(4)
'''THIS AINT NO BIGGIE YOU GOT THIS. BE CALM AND THINK THROUGH IT ALL'''

