'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading
import time

class MyThread(threading.Thread):
    def do_a(self):
        r_lock.acquire()
        print(self.name, "got lock a", time.ctime())
        time.sleep(3)
        r_lock.acquire()
        print(self.name, "got lock b", time.ctime())
        r_lock.release()
        r_lock.release()

    def do_b(self):
        r_lock.acquire()
        print(self.name, "got lock b", time.ctime())
        time.sleep(3)
        r_lock.acquire()
        print(self.name, "got lock a", time.ctime())
        r_lock.release()
        r_lock.release()

    def run(self):
        self.do_a()
        self.do_b()

if __name__ == '__main__':
    r_lock = threading.RLock()
    threads = []
    for i in range(5):
        threads.append(MyThread())
    for t in threads:
        t.start()
