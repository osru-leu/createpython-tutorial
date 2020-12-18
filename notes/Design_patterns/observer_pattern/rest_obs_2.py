
# 1.  getattr(who, 'update', None) if an 'update' method cant be found in the -who- object we can add
# a default value in the None parameter space. If no value is added, then the parameter is set to None.

class FohSubscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
class BohSubscriber:
    def __init__(self, name):
        self.name = name
    def recieve(self, message):
        print('{} got message "{}"'.format(self.name, message))
#register subscriberTwos receive method with the publisher

class ManagementPublisher:
    def __init__(self):
        self.subscribers = dict()
    def register(self, who, callback=None):
        """ the callback parameter is optional and if its not supplied, fall back to the original """
        if callback is None:
            callback = getattr(who, 'update') #NOTE 'update' is calling to the update method
        self.subscribers[who] = callback
    def unregister(self, who):
        del self.subscribers[who]
    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items(): #items()returns a list of dictionary items, key:value pair
            callback(message)


management = ManagementPublisher()

bob = FohSubscriber('Bob')
tom = BohSubscriber('Tom')
hoestist = FohSubscriber('hoe')

management.register(bob, bob.update)
management.register(tom, tom.recieve)
management.register(hoestist)

management.dispatch('Bring yo asses to the meeting')
management.unregister(tom)
management.dispatch('Foh come sober damnit')

