'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

from collections import Iterable

class MyClass(object):
    def __iter__(self):
        return self

c1 = MyClass()
result = isinstance(c1, Iterable)
print(result)