'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time

def work1(queue):
    for i in range(10):
        print("+++进程1向queue添加数据：", i)
        queue.put(i)
        queue.put(i)
        queue.put(i)
        time.sleep(0.5)

def work2(queue):
    try:
        while True:
            value = queue.get(time = 3)
            print("---进程2从queue获取数据", value)
    except:
        print("3秒之内没有获取到数据，主动关闭自己")

if __name__ == '__main__':
    queue = multiprocessing.Queue(5)

    p1 = multiprocessing.Process(target=work1, args=(queue,))
    p2 = multiprocessing.Process(target=work2, args=(queue,))
    p1.start()
    p2.start()

    print("主进程...")