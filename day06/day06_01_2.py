'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

from collections import Iterable

result = isinstance([1, 2], Iterable)
print(result)

result = isinstance((1, 2), Iterable)
print(result)

result = isinstance("hello", Iterable)
print(result)

result = isinstance({"a": 10, "b": 100}, Iterable)
print(result)

result = isinstance(100, Iterable)
print(result)

class MyClass(object):
    pass

c1 = MyClass()
result = isinstance(c1, Iterable)
print(result)