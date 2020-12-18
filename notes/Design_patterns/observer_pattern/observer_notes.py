#http://wwww.geeksforgeeks.org/observer-method-python-design-patterns/

# Observer method
'''
The observer method is a Behavioral design Pattern which allows you to define or create a subscription
mechanism to send the notification to the multiple objects about any new event that happens to the object
that they are observing. The subject is basically observed by multiple objects. The subject needs
to be monitored and whenever there is a change in the subject, the observers ae being notified about
the change. This pattern defines one to many dependencies between objects so that one object changes state,
all of its dependents are notified and updated automatically.
'''
# Problem without using observer method
'''
Imagine you want to create a calculator application that has different features such as addition, subtraction
changing base of the numbers to hexadecimal, decimal, and many other features. But one of your friends is 
interested in changing the base of his favorite number to Octal base number and you are still
developing the application. So, what could be the solution to it? Should your friend check the application
daily just to get to know about the status? But dont you think it would result in a lot of unneccesary 
visits to the application which were definitely not required. Or you may think about that each time you
add the new feature and send the notification to each user. Is it ok? Sometimes yes but not every time.
Might be some users get offended by a lot of unnecessary notifications which they really don't want.

                        subscriber---------->Publisher <-----------subscriber

                        All objects that want to track changes in the publishers state
                        are called subscribers.
'''

class Subject:
    ''' Represents what is being observed '''
    def __init__(self):
        ''' Create and empty observer list '''
        self._observer  = []

    def notify(self, modifier=None):
        ''' Alert the observers '''
        for observer in self._observer:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        ''' If the observer not in the list, 
        append it into the list '''
        if observer not in self._observer:
            self._observer.append(observer)

    def detach(self, observer):
        ''' Remove the observer from the observer list '''
        try:
            self._observer.remove(observer)
        except ValueError:
            pass

class Data(Subject):    # OBSERVABLE
    ''' Monitor the object '''
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class HexViewer: # OBSERVERS
    ''' Updates the Hew viewer '''
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

class OctalViewer:
    ''' Updates the Octal viewer '''
    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) + 'has data' + str(oct(subject.data)))

class DecimalViewer:
    ''' Update the Decimal viewer '''
    def update(self, subject):
        print('DecimalViewer: Subject %s has data % d' % (subject.name, subject.data))

''' Main function '''

if __name__ == "__main__":

    ''' Provide the data '''
    obj1 = Data('Data 1')
    obj2 = Data('Data 2')

    view1 = DecimalViewer()
    view2 = HexViewer()
    view3 = OctalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 10
    obj2.data = 15

