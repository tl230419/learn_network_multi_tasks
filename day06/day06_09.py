'''
*****************
Date: 2020-04-28
Author: Allen
*****************
'''

from greenlet import greenlet
import time

def test1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)
        print("sleep a")

def test2():
    while True:
        print("---B---")
        gr1.switch()
        time.sleep(0.5)
        print("sleep b")

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()