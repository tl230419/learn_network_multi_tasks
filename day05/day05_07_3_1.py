'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing

queue = multiprocessing.Queue(3)
queue.put(1)
queue.put("hello")
queue.put([1, 2, 3])
print(queue)

value1 = queue.get()
print(value1)

value2 = queue.get()
print(value2)

value3 = queue.get()
print(value3)
