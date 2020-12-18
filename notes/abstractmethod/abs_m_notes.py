from abc import ABC, abstractmethod
# Important points about abstract classes in python

#1. Abstract classes can have both concrete methods as well as abstract methods.
#2. Abstract classes work as a template for other classes. Using an abstract class you 
#   can define a generalized structure without providing complete implementation of every method.
#3. Abstract classes cant be instantiated so it is not possible to create objects of an abstract class.
#4. Generally abstract methods defined in abstract classes dont have body but it is possible to have 
#   abstract methods with implementation in abstract classes. Any sub class deriving from such
#   abstract classes still need to provide implementation for such abstract methods.
#5. If any abstract method is not implemented by the derived class Python throws an error.
class Parent(ABC):
    #common functionality
    def common(self):
        print('In common method of Parent')
    @abstractmethod
    def vary(self):
        print('In vary method of Parent')

class Child(Parent):
    pass

# object of Child1 class
obj = Child() # Throws error:
'''Traceback (most recent call last):
File "c:/Users/ursos/Documents/Python/createpython-tutorial/notes/abstractmethod/abs_m_notes.py", line 24, in <module>
    obj = Child()
TypeError: Can't instantiate abstract class Child with abstract methods vary
'''
obj.common()
obj.vary()

# You must implement def vary() in the child class for the above code to work