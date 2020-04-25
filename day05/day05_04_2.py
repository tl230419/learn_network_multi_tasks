'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing

num = 100

def work():
    global num
    num += 1
    print("work num = %d" % num)

def work2():
    print("work2 num = %d" % num)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work)
    p1.start()

    p2 = multiprocessing.Process(target=work2)
    p2.start()