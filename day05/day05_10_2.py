'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time

def write_queue(queue):
    for i in range(5):
        print("正在写入：", i)
        queue.put(i)
        time.sleep(1)

def read_queue(queue):
    while True:
        try:
            value = queue.get(timeout = 3)
            print("读取到queue的值：", value)
        except:
            print("超过3秒没获取到数据，停止循环")
            break

if __name__ == '__main__':
    pool = multiprocessing.Pool(2)

    queue = multiprocessing.Manager().Queue(3)

    pool.apply_async(func=write_queue, args=(queue,))
    pool.apply_async(func=read_queue, args=(queue,))

    pool.close()
    pool.join()