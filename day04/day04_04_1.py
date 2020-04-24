'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import threading
from time import sleep, ctime

def sing(a, b, c):
    print("----sing----a = %d, b = %d, c = %d" % (a, b, c))
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)

if __name__ == '__main__':
    print("---开始---:%s" % ctime())

    # pass param 1: args
    #t1 = threading.Thread(target=sing, args=(10, 100, 1000))
    # pass param 2: kwargs
    t1 = threading.Thread(target=sing, kwargs={"a": 10, "b": 100, "c": 1000})
    # both args and kwargs
    t1 = threading.Thread(target=sing, args=(10, ), kwargs={"b": 100, "c": 1000})
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为： %d' % length)
        if length <= 1:
            break

        sleep(0.5)

    print("---结束---:%s" % ctime())