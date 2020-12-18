#http://www.python-course.eu/python3_abstract_classes.php

class AbstractClass:

    def do_something(self):
        pass

class B(AbstractClass):
    pass
 
a = AbstractClass()
b = B()

# Running this returns nothing

# If we start this program, we see that this is not an abstract class, because:
#   -we can instantiate an instance from
#   -we are not required to do_something in the class definition of B


# Our example implemented a case of simple inheritance which has nothing to do with an abstact class.
# In fact, Python o its own doesn't provide abstract classes. Yet, Python comes with a module which provides
# the infrastructure for defining Abstract Base Classes (ABCs). This module is called- abc.

# The following Python code uses the abc module and defines an abstract base class:

from abc import ABC, abstractmethod
''
class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

        @abstractmethod
        def do_something(self):
            pass''

#We will define now a subclass using the previously defined abstract class. You will notice that we havent't 
# implemented the do_something method, even though we are required to implement it, because
# this method is decorated as an abstract method with the decorator"abstractmethod". we get an exception
# that DoAdd42 can't be instantiated


# class Doadd42(AbstractClassExample):
#     pass

# x = Doadd42(4)

# We will do it the correct way in the following example, in which we define two classes inheriting from 
# our abstract class:

class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42

class DoMul42(AbstractClassExample):

    def do_something(self):
        return self.value * 42

x = DoAdd42(10)
y = DoMul42(10)

print(x.do_something())
print(y.do_something())

# A class that is derived from an abstract class cannot be instantiated unless all of its abstract
#  methods are overridden.

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print('Some implementation')

class AnotherSubClass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print('The enrichment from AnotherSubclass')


x = AnotherSubClass()
x.do_something()




