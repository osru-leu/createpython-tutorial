def is_type_valid(lliquor_type):
    VALID_TYPES = ['VODKA', 'TEQUILA']
    if liquor_type.lower() in VALID_TYPES
        return True
    return False



if __name__ == "__main__":
    STORE = []
    
    if not is_type_valid('vodkas'):
        print('Type is not valid, try again.')
    exit()
    while True:
        if len(STORE) >= 2:
            print('Warehouse is full !!!')
            break
        ACTION = input('What do you want to do (add / exit)? ')
        if ACTION.lower() == 'exit':
            break
        if ACTION.lower() != 'add':
            print(f'{ACTION} is not a valid command.\n')
            continue
        NAME = input('What brand? ')
        TYPE = input('What type? ').upper()
        PRICE = input('What price? ')
        PRICE = float(PRICE)
        ID = len(STORE)
        STORE.append({
            'id': ID,
            'name': NAME,
            'type': TYPE,
            'price': PRICE
        })

    print(f'\nYour inventory is: \n{STORE}')
