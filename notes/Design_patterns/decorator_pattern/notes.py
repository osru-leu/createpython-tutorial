#http://www.youtube.com/watch?v=AHVMObEokNw

'''
Decorator Pattern Def:
    Attaches addtional responsibilities to an object dynamically.
    Decorators provide a flexible alternative to subclassing for 
    extending functionality.

    Subclassing for extended functionality:
        You have an animal class with a speak method then a dog subclass that overrides the speak method
        so that when the dog speak()s it 'barks'. Then you have a cat subclass and when it overrides the speak()
        it 'meows'
    Class Explosion:
       
Main takeaway:
    By using the decorator pattern you can impersonate a class
    and add additional functionality to it without any of the users 
    of that class knowing that its any different than the original 
    class.
'''

subclasses = ([cls.__name__ for cls in Addon.__subclasses__()])
if choice not in subclasses:
    print(f'Type %s not a subclass of Addon', choice)
    print(f'Valid choices are {subclasses}')
else:
    globals()[addons](base)
