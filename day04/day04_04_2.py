'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import threading
from time import sleep, ctime

def sing():
    for i in range(3):
        print("---------------------------")
        sleep(1)

def dance():
    for i in range(3):
        print("--------")
        sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()