'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import threading
import sys
import requests
import time
import os

class MulThreadDownload(threading.Thread):
    def __init__(self, url, start_pos, end_pos, f):
        super(MulThreadDownload, self).__init__()
        self.url = url
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.fd = f

    def download(self):
        print("start thread:%s at %s" % (self.getName(), time.time()))
        headers = {"Range" : "bytes=%s-%s"%(self.start_pos, self.end_pos)}
        res = requests.get(self.url, headers=headers)
        self.fd.seek(self.start_pos)
        self.fd.write(res.content)
        print("stop thread:%s at %s" % (self.getName(), time.time()))

    def run(self):
        self.download()

if __name__ == '__main__':
    url = sys.argv[1]
    file_name = url.split('/')[-1]
    file_size = int(requests.head(url).headers['Content-Length'])
    print("%s filesize:%s" % (file_name, file_size))

    thread_num = 3
    threading.BoundedSemaphore(thread_num)
    step = file_size // thread_num
    mtd_list = []
    start = 0
    end = -1

    temp_f = open(file_name, 'w')
    temp_f.close()
    with open(file_name, 'rb') as f:
        file_no = f.fileno()
        while end < file_size - 1:
            start = end + 1
            end = start + step - 1
            if end > file_size:
                end = file_size

            dup = os.dup(file_no)
            fd = os.fdopen(dup, 'rb+', -1)
            t = MulThreadDownload(url, start, end, fd)
            t.start()
            mtd_list.append(t)

        for i in mtd_list:
            i.join()