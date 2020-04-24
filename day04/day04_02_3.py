'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import time
import threading

def say_sorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=say_sorry)
        t1.start()

    print("我是主线程")