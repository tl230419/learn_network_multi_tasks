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
        lock_a.acquire()
        print(self.name, "got lock a", time.ctime())
        time.sleep(3)
        lock_b.acquire()
        print(self.name, "got lock b", time.ctime())
        lock_b.release()
        lock_a.release()

    def do_b(self):
        lock_b.acquire()
        print(self.name, "got lock b", time.ctime())
        time.sleep(3)
        lock_a.acquire()
        print(self.name, "got lock a", time.ctime())
        lock_a.release()
        lock_b.release()

    def run(self):
        self.do_a()
        self.do_b()

if __name__ == '__main__':
    lock_a = threading.Lock()
    lock_b = threading.Lock()

    threads = []
    for i in range(5):
        threads.append(MyThread())
    for t in threads:
        t.start()
