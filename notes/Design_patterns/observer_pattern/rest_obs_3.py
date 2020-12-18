# finish the code then come back to #NOTE 1 and define what is going on here. try refering to the the video


class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

class Publisher:
    def __init__(self, events):
        '''subscriber attribute is seeded as a dictionary, mapping event names, which will just be strings
        to dictionaries which will map subscriber objects to the callback method for that particular event'''
        self.subscribers = { event : dict() #NOTE 1 event is set only to dictionary values? #dictionary comprehension
                            for event in events} 
    def get_subscribers(self, event):
        return self.subscribers[event]
    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback
    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
