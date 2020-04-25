'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing

def test(a, b, c):
    print(a, b, c)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=test, args=(10, 20, 30))
    p1.start()

    p2 = multiprocessing.Process(target=test, args=(10, ), kwargs={"b": 20, "c": 30})
    p2.start()