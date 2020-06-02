# """ Bar """
from inventory import get_inventory, add_item, remove_item_by_name, find_item_name, find_item_type
# import inventory

if __name__ == "__main__":

    print('Welcome to the Python Bar Inventory Application.')

    while True:
        ACTION = input('What action would you like to perform (list/add/find/delete/exit)?').lower().strip(' ')
        if ACTION == 'list':
            print(get_inventory())
            continue
        
        if ACTION == 'find':
            ACTION_ACTION = input('Would you like to find by (name/type)? ').lower()

            if ACTION_ACTION == 'name':
                NAME = input('What is the name? ').lower()
                ITEM = find_item_name(NAME)
                if ITEM:
                    print(ITEM) # <--needs to print specific to names 
                else:
                    print(f"Item {ITEM} not in inventory")
            elif ACTION_ACTION == 'type':
                TYPE = input('What is the type? ').upper()
                ITEMS = find_item_type(TYPE)
                if ITEMS:
                    print(ITEMS) # <--- needs to print specific to types
                else:
                    print(f'{ITEM} not in inventory')
                    
            else:
                print(f'{ACTION_ACTION} is not a valid command.')
           
        elif ACTION == 'add':
            NAME  = input( 'What is the name? ')
            TYPE = input( 'What is the item type? ').upper()
            PRICE = input ('What is the price? ' )
            add_item({'name': NAME, 'type': TYPE, 'price': PRICE})

        if ACTION == 'delete':
            NAME  = input( 'What is the name? ')
            
            remove_item_by_name(NAME)
            

        elif ACTION == 'exit':
            print('Thank you for using Python Bar Inventory.')
            break
        else:
            print(f'{ACTION} is not valid.')
    
    #       ADD OPTION TO DELETE ENTIRE INVENTORY INSTEAD OF GOING THROUGH AND REMOVING ONE BY ONE
    #       NOTIFY USER WHEN INVENTORY IS VOID OF PRODUCT 
    #        - if user tries to use the delete function here prompt them that there is nothing in inventory so deletion is not an option
    



















    # while True:
    #     INVENTORY=[]
    #     ACTION = input('What action would you like to perform (list/add/delete/exit)?' ).lower()
    #     if ACTION.lower() == 'exit':
    #         break
    #     if ACTION.lower() == 'add':
    #         ITEM = add_item(item)
      
       
    #     print(f' your added item: {INVENTORY}')
    #     if ACTION == 'list':
    #         print(get_inventory)
            
    #     #if action == 'delete':
    #     #     CALL REMOVE_ITEM FUNCTION

        
        
        
    
    # else:
    #     print('Thank you for using Python Bar Inventory.')
    #     #------------NEW CODE ABOVE -----------------------------------------------------------------------#
    # print('------------- INVENTORY -----------------')
    # print(get_inventory())
    # print('-----------------------------------------')

    # # This first item we are adding already exists in the inventory
    # add_item({'name': 'Titos', 'type': 'VODKA', 'price': 13.07})

    # # This second item we are adding does not exist in the inventory yet
    # add_item({'name': 'Absolute', 'type': 'VODKA', 'price': 11.27})

    # print('------------- INVENTORY -----------------')
    # print(get_inventory())
    # print('-----------------------------------------')

    # # Remove an item thatis in the list
    # remove_item_by_name('Titos')

    # print('------------- INVENTORY -----------------')
    # print(get_inventory())
    # print('-----------------------------------------')

    # # Example of creating a dictionary from inputs and adding it to inventory
    # ITEM_NAME = input('Name: ')
    # ITEM_TYPE = input('Type: ')
    # ITEM_PRICE = input('Price: ')

    # add_item({'name': ITEM_NAME, 'type': ITEM_TYPE, 'price': ITEM_PRICE})

    # print('------------- INVENTORY -----------------')
    # print(get_inventory())
    # print('-----------------------------------------'