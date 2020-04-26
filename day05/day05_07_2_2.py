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

queue.get()
queue.get()
queue.get()

queue.get()
