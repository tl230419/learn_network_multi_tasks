'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading
import time

event = threading.Event()
event.set()

def lighter():
    counter = 0
    while True:
        if 5 < counter <= 10:
            event.clear()
            print("\33[41;1m 红灯... \033[0m")
        elif counter > 10:
            event.set()
            counter = 0
        else:
            print("\33[42;1m 绿灯... \033[0m")
        counter += 1
        time.sleep(1)

def car():
    while True:
        if event.is_set():
            print("小车运行中...")
            time.sleep(1)
        else:
            print("小车等红灯中...")
            event.wait()
            print("绿灯亮了，小车启动啦！...")

if __name__ == '__main__':
    lighter_thread = threading.Thread(target=lighter)
    lighter_thread.start()

    car_thread = threading.Thread(target=car)
    car_thread.start()