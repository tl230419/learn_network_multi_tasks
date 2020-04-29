'''
*****************
Date: 2020-04-27
Author: Allen
*****************
'''

import time

def work1():
    while True:
        print("正在执行work1---------------------")
        time.sleep(0.5)
        yield

def work2():
    while True:
        print("正在执行work2---------------------")
        time.sleep(0.5)
        yield

if __name__ == '__main__':
    w1 = work1()
    w2 = work2()

    while True:
        next(w1)
        next(w2)