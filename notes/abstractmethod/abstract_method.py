# http://www.youtube.com/watch?vUDmJGvM-OUw

#what is an abstract method?
#   an abstract method does not have a declaration it has a definition
    # and abstract class?
#       a class that has abstract methods

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('its running')

class Whiteboard(Computer):
    def write(self):
        print('its writing')

class Programmer:
    def work(self, com):
        print('solving problems')
        com.process()
#com = Computer()
com1 = Laptop()
com2 = Whiteboard()
#com.process()
prog1 = Programmer()
prog1.work(com2)
#com1.process()