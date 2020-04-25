'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

from concurrent.futures import ThreadPoolExecutor
import time

def say_hello(a):
    print("hello: ", a)
    time.sleep(2)

if __name__ == '__main__':
    seed = range(10)

    with ThreadPoolExecutor(3) as executor:
        for each in seed:
            executor.submit(say_hello, each)

    with ThreadPoolExecutor(3) as executor1:
        executor1.map(say_hello, seed)