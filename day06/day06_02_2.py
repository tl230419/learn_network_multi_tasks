'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

data_list = [1, 3, 5, 7, 9]
data_list_iterator = iter(data_list)
print(data_list_iterator)

value = next(data_list_iterator)
print("value1 = ", value)

#for i in range(5):
    #value = next(data_list_iterator)
    #print("value = ", value)

from collections import Iterator

result = isinstance([], Iterator)
print(result)

result = isinstance(iter([]), Iterator)
print(result)

result = isinstance(iter("abc"), Iterator)
print(result)