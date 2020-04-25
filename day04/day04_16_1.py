'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading
import multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

def mutex_test():
    lock = threading.Lock()
    for i in range(100000):
        lock.acquire()
        try:
            #change_it()
            print("")
        finally:
            lock.release()

        with lock:
            try:
                # change_it()
                print("")
            except Exception as e:
                print("Exception: ", e)

if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    print("CPU:", count)

    # for i in range(count):
    #     t = threading.Thread(target=loop)
    #     t.start()

    for i in range(count):
        t = multiprocessing.Process(target=loop)
        t.start()