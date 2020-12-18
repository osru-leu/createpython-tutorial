
class SubscriberOne:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

class SubscriberTwo:
    def __init__(self, name):
        self.name = name
    def receive(self, message):
        print('{} got message "{}"'.format(self.name, message))

class Publisher:
    def __init__(self):
        self.subscribers = dict()
    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback
    def unregister(self, who):
        del self.subscribers[who]
    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)


pub = Publisher() # create publisher object

bob = SubscriberOne('Bob') # create subscribers
alice = SubscriberTwo('Alice')
john = SubscriberOne('John') 

pub.register(bob, bob.update)# register subscribers with the publisher #NOTE sigining up for an app?
pub.register(alice, alice.receive)
pub.register(john)

pub.dispatch('It\'s lunch time!')

pub.unregister(john)
pub.dispatch('Time for dinner')


    