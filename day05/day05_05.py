'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time

def sub_process():
    for i in range(10):
        print("子进程运行中", i)
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sub_process)
    p1.daemon = True
    p1.start()

    time.sleep(2)
    print("Over")
    p1.terminate()
    exit()