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

print("取值前消息数量：", queue.qsize())
value1 = queue.get()
print(value1)
print("取值后消息数量：", queue.qsize())

result = queue.empty()
print(result)