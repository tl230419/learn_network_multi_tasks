'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import time

def process_recevier(pipe):
    while True:
        data = pipe.recv()
        print("pipe -> recv: \33[42;1m 接收 \033[0m", data)

def process_sender(pipe):
    for i in range(100):
        print("send -> pipe: \33[41;1m 发送 \033[0m", i)
        pipe.send(i)
        time.sleep(1)

if __name__ == '__main__':
    pipe = multiprocessing.Pipe(duplex=False)
    p_sender = multiprocessing.Process(target=process_sender, args=(pipe[1],))
    p_receiver = multiprocessing.Process(target=process_recevier, args=(pipe[0],))

    p_sender.start()
    p_receiver.start()