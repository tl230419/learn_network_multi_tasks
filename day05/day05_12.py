'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import os

print("主进程 {} 已开启...".format(os.getpid()))
pid = os.fork()
if pid == 0:
    print("我是子进程 {} 我的父进程是{}".format(os.getpid(), os.getppid()))
else:
    print("我是父进程 {} 我刚创建了个子进程{}".format(os.getpid(), pid))