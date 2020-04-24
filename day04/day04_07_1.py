'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        # Call father's init function
        super(MyThread, self).__init__()
        self.num = num

    # Rewrite father's run function
    def run(self):
         for i in range(5):
             print("正在执行run方法...", self.name, i)
             time.sleep(0.5)

    def test(self):
        pass

if __name__ == '__main__':
    my_thread = MyThread(10)
    my_thread.start()