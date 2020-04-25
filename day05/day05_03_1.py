'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time

def work1():
    for i in range(10):
        print("work1----", i, multiprocessing.current_process())
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = multiprocessing.Process(group=None, target=work1)
    p1.start()

    for i in range(10):
        print("这是主进程", i)
        time.sleep(0.5)