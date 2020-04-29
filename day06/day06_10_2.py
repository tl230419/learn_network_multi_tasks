'''
*****************
Date: 2020-04-28
Author: Allen
*****************
'''

import  time
import gevent
from gevent import monkey
monkey.patch_all()

def work1():
    for i in range(5):
        print("work1---1")
        time.sleep(0.5)
        print("work1", gevent.getcurrent())

def work2():
    for i in range(5):
        print("work2---2")
        time.sleep(0.5)
        print("work2", gevent.getcurrent())

g1 = gevent.spawn(work1)
g2 = gevent.spawn(work2)



g1.join()
g2.join()