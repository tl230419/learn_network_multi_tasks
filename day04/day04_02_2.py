'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

# Single thread
import time

def say_sorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        say_sorry()