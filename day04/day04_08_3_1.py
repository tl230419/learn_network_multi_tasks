'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading
import time

num = 0

def work1():
    global num

    #for i in range(100):
    for i in range(1000000):
        num += 1

    print("work1 num = %d" % num)


def work2():
    global num

    # for i in range(100):
    for i in range(1000000):
        num += 1

    print("work2 num = %d" % num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("num = ", num)
