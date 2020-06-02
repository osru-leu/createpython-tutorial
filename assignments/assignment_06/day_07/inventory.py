""" Inventory """
INVENTORY = [
    {'name': 'stoli', 'type': 'VODKA', 'price': 123.07},
    {'name': 'patron', 'type': 'TEQUILA', 'price': 124.97},
    {'name': 'titos', 'type': 'VODKA', 'price': 13.07}
]
TOTAL_INV = []

def get_inventory():
    """ This returns the inventory """
    return INVENTORY

def find_item_name(name):
    for i in get_inventory():
        
        if name.lower() == i['name'].lower():
            #print(all('name'))
            #print(f"your items found {i['name']}")
            #INVENTORY.???(name)
            return i
    # else:
    #     print(f"{name} is not in inventory")# MOVE TO BAR.PY

def find_item_type(type):
    # Create an empty list first <-- list of all the items that match type
    # Loop thru all the items, if the item matches the type... then add it to the list
    items_found = []
    for i in get_inventory():
        if type.upper() == i['type'].upper(): 
            items_found.append(i)
            
    return items_found
        

def add_item(item):
    """ Add a new item to the inventory """
    # Check first if the item already exists in the inventory
    for i in get_inventory():
        if i['name'].lower() == item['name'].lower():
            print(f"[ERROR] item with name {i['name']} already exists")
            break
    else:
        print(f'[INFO] Adding item {item}')
        INVENTORY.append(item)
        # mongo.collection().insert_one(item)


def remove_item(item):
    """ Remove an item """
    INVENTORY.remove(item)
   

def remove_item_by_name(name):
    """ Remove an item with thename specified """
    
    item_found = False
    for item in INVENTORY.copy():
        if name.lower() == item['name'].lower():
            item_found = True
            print(f'[INFO] Removing item {item}')
            remove_item(item)
        if INVENTORY == TOTAL_INV:
            print('You now have 0 items in inventory')
            break

    if not item_found:
        print(f'Sorry, we did not find {name} in inventory.')

