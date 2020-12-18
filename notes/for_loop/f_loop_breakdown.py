a = ['foo', 'bar', 'baz']

for i in a:
    print(i)

#output
#foo
#bar
#baz

''' In this for loop Python does the following:

-Calls iter() to obtain an iterator for -a-
-Calls next() repeatedly to obtain each item from the iterator in turn
-Terminates the llp when next() raises the StopIteration exception

The loop body is exectued once for each item next() returns, with loop variable i set
to the given item for each iteration:

a = ['foo', 'bar', 'baz'] ----> iter()-> itr = iter(a) -> next(itr) -> 'foo'
                                                       -> next(itr) -> 'bar'
                                                       -> next(itr) -> 'baz'
                                                       -> next(itr) ---------> StopIteration

Memory recall/review:

So, a basic for loop calls a short list of built in functions in python:
iter()
next()
'''
b = [('a', 1), ('b', 2), ('c', 3)]
''' i = first value of a tuple
    j = 2nd value of the same tuple
'''
for i, j in b:
    print(i, j)
# output:
'''
a 1
b 2
c 3


'''
# iterating through a dictionary for value and key:

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print('k =', k, 'v =', v)

#output:
'''
k = foo v = 1
k = bar v = 2
k = baz v = 3
'''