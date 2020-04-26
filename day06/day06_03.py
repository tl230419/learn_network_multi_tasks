'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

from collections import Iterable

class MyList():
    def __init__(self):
        self.item = list()

    def add_item(self, data):
        self.item.append(data)

    def __iter__(self):
        my_list_iterator = MyListIterator(self.item)
        return my_list_iterator

class MyListIterator():
    def __init__(self, item):
        self.item = item

        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_index < len(self.item):
            data1 = self.item[self.current_index]
            self.current_index += 1
            return data1
        else:
            raise StopIteration

if __name__ == '__main__':
    my_list = MyList()
    my_list.add_item("张三")
    my_list.add_item("李四")
    my_list.add_item("王五")

    result = isinstance(my_list, Iterable)
    print(result)

    for value in my_list:
        print(value)

