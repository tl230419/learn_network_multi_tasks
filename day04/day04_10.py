'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading
import time

g_num = 0

def test1(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("test1 g_num = %d" % g_num)


def test2(num):
    global g_num

    mutex.acquire()
    for i in range(num):
        #mutex.acquire()
        g_num += 1
        #mutex.release()
    mutex.release()

    print("test2 g_num = %d" % g_num)

if __name__ == '__main__':
    mutex = threading.Lock()

    t1 = threading.Thread(target=test1, args=(100000,))
    t1.start()

    t2 = threading.Thread(target=test2, args=(100000,))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("result:%s", g_num)
