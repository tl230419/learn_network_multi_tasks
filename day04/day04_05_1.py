'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import threading
import time

def work1():
    for i in range(10):
        print("正在执行...", i)
        time.sleep(0.5)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t1.setDaemon(True)
    t1.start()

    time.sleep(2)
    print("Game Over")
    exit()