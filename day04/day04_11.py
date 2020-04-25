'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading

lock = threading.Lock()

def get_value(index):
    data_list = [1, 3, 5, 7, 9]
    lock.acquire()
    if index >= len(data_list):
        print("%d 下标越界" % index)
        lock.release()
        return
    print(data_list[index])
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        t1 = threading.Thread(target=get_value, args=(i,))
        t1.start()