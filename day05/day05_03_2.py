'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time
import os

def work():
    print(multiprocessing.current_process())
    print("父进程id: ", os.getppid())
    print(multiprocessing.current_process().pid, os.getpid())

    i = 0
    while i < 10:
        print("work中执行", i)
        time.sleep(0.5)
        i += 1

if __name__ == '__main__':
    p1 = multiprocessing.Process(group=None, target=work)
    p1.start()

    for i in range(10):
        print("这是主进程", i)
        time.sleep(0.5)