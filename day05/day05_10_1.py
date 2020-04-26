'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time

def write_data(queue):
    for i in range(5):
        if queue.full():
            print("队列已满！")
            break

        queue.put(i)
        print("正在写入：", i)
        time.sleep(0.2)

def read_data(queue):
    while True:
        if queue.qsize() == 0:
            print("队列为空!")
            break

        result = queue.get()
        print(result)
        time.sleep(0.2)

if __name__ == '__main__':
    pool = multiprocessing.Pool(2)

    queue = multiprocessing.Manager().Queue(3)

    result = pool.apply_async(write_data, args=(queue,))
    result.wait()
    pool.apply_async(read_data, args=(queue,))

    pool.close()
    pool.join()