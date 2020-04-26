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

result = queue.full()
print(result)

queue.put([1, 2, 3])

result = queue.full()
print(result)