#Iterating through a dictionary and returning key and value

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key, '->', a_dict[key]) #NOTE a_dick[key] gives you the value
                                    #NOTE dictionaryname[key name] = the value of the key
'''
color -> blue
fruit -> apple
pet -> dog
'''

''' One of the most useful ways to iterate through a dictionary in python is by using .items(),
    which is a method that returns a new view of the dictionary's items:
'''

d_items = a_dict.items()
print(d_items)
''' This returns a list of tuples of the keys and their values:

    dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
        '''
# For looping items()
for item in a_dict.items():
    print(item)
''' ('color', 'blue')
    ('fruit', 'apple')
    ('pet', 'dog') '''

# For looping .items() and returning type()
for item in a_dict.items():
    print(type(item))
''' ('color', 'blue')
    ('fruit', 'apple')
    ('pet', 'dog')
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'> '''

''' You can use tuple unpacking to iterate through the keys and values of
the dictionary you are working with. to achieve this, you just need to unpack the elements
of every item into two different variables representing the key and the value:
'''

for key, value in a_dict.items():
    print(key, '->', value)

''' color -> blue
    fruit -> apple
    pet -> dog '''

''' Here, the variables -key- and -value- in the header of your for loop do the unpacking. Every time
the loop runs, -key- will store the key, and -value- will store the value of the item that has 
been processed. This way, you'll have more control over the items of the dictionary, and
you'll be able to process the keys and values separately and in a way that is more readable
and Pythonic. '''

#NOTE .values() and .keys() return view objects just like.items()

# Iterating through .keys()

''' If you just need to work with the keys of a dictionary, then you can use .keys(), 
which is a method that returns a new view object containing the dictionary's keys: '''


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
print(keys)
''' dict_keys(['color', 'fruit', 'pet']) '''


# Using the same trick as before (indexing operator[]), you can get access
# to the values of the dictionary:

for key in a_dict.keys():
    print(key)
'''
color
fruit
pet
'''

# Iterating Through.values()

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
values = a_dict.values()
print(values)
'''
dict_values(['blue', 'apple', 'dog'])
'''
''' In the previous code, -values- holds a reference to a VIEW OBJECT containing the values of
a_dict
'''

# .values() yields the values of a_dict:

for value in a_dict.values():
    print(value)
'''
blue
apple
dog
'''
#NOTE it's worth noting that they also support membership tests (in), which is an important feature 
# if you're tryiing to know if a specific element is in a dictionary or not:

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
pet_key = 'pet' in a_dict.keys()
print(pet_key)
'''
True'''

fruit_value = 'apple' in a_dict.values()
print(fruit_value)
'''
True
'''
false_value = 'onion' in a_dict.values()
print(false_value)
'''
False
'''

#MODIFYING VALUES AND KEYS:

''' The values can be modified whenever you need, but you'll need to use the original
dictionary and the key that maps the value you want to modify: '''

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2) # Apply 10% discount. prices[k] points to the value of each key
#                                   in prices{}

# -------loop breakdown --------
print(f'prices[k]: {prices[k]} the last key: value in the list')
print(f'k: {k}')
print(f'v: {v}')
print(f'Prices after discount: {prices}')
#---------------OR YOU COULD WRITE IT LIKE:----------------#

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for item, price in prices.items():
    prices[k] = round(price * 0.9, 2) 

''' In the original loop, to modify the values of -prices- and apply a 10% discount, you
used the expression prices[k] = round(v * 0.9, 2).
k and v changes done inside of the for loop are not reflected in the original dictionary. If you
modify them inside of the loop, then what happens is that you'll lose the reference to the relevant 
dictionary component without changing anything in the dictionary '''

''' On the other hand, the keys can be added or removed frrom a dictionary by converting the view
returned by .keys() into a list object: '''

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()): # Use a list instead of a view
    if key == 'orange':
        del prices[key] # Delete a key from prices
print(prices)
'''
{'apple': 0.4, 'banana': 0.25}
'''


class Dog:

    # Class variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):
        # Instance variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

Rodger = Dog('Pug') #instantiate
Rodger.setColor('brown') # set instance variable
print(Rodger.getColor()) # get instance variable