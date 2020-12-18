# management-publisher
# chefs-publisher
# foh_emps-subscriber
# boh_emps-subscriber
''' This code uses the set() function:
    set()
        - creates a set object. 
        - object is iterable
        - used to store multiple items to a single variable
        - set collection is both unordered and unindexed
    set() uses many functs. In this program:
        - discard(): removes an item from a set
        - add(): adds an item to a set
        - update(): updates current set by adding items from another set
            If an item is present in both sets, only 1 of that item will
            be in the updated set.
'''
class BohSubscribers:#NOTE later, unsubscribe boh from foh messages
    ''' Observer class- kitchen'''
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

class FohSubscribers:#NOTE later, unsubscribe foh from boh messages
    ''' Observer class- Front of the house '''
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

    


class ManagementPublisher:
    ''' Observable class '''
    ''' Call the class then the method desired:
        class_name.method(parameter)
        or set the class
        to a variable and call the variable then the method. '''
    def __init__(self):
        self.subscribers = set() # NOTE creates an empty set- keeps track of whats going on
    def register(self, who):
        ''' adding a subscriber, ex: bob = ManagementPublisher.register(bob) '''
        self.subscribers.add(who) 
    def unregister(self, who):
        ''' to use: ManagementPublisher.unregister(bob) '''
        self.subscribers.discard(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)
        ''' for each subscriber in subscribers(A set() of subscribers),
                send message. '''


management = ManagementPublisher()

dick = FohSubscribers('Dick')# subscribe dick to FOH Portal
Tom = BohSubscribers('Tom')
Hoestist = FohSubscribers('Hoestist')

management.register(dick) #register dick to receive messages
management.register(Tom)
management.register(Hoestist)

management.dispatch('All Staff meeting the 14th')
management.unregister(Tom)
management.dispatch('Foh come sober')



'''
Quiz muhself:

What would you need to make this work?

a publsher class
a subscriber class

a def __init__ for both.

a self.name = name for subscriber
a self.subscriber = set() for publisher __int__

a register method - publisher class
a unregister method - publisher class
a dispatch method - publisher class

you're going to use functs such as:
update()
add()
discard()
set()
'''
# Further breakdown with reference(when stuck) to actual code

'''
In the subscriber class
def __init__(self, name):
    self.name = name

def update(self, message): NO NEED FOR MESSAGE PARAMETER HERE. MESSAGE PARAMETER FOR DISPATCH METHOD
    the message you would like to return

In the Publisher class
def __init__(self):
    self.subscriber = set()

def register(self, who): 
    self.subscriber.add(who)

def unregister(self, who):
    self.subscriber.discard(who)

def dispatch(self, message):
    for subscriber in self.subscribers:
        self.subscriber.update(message)
'''




