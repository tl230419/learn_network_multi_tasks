'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

from queue import *
import threading
import urllib
import time
import json
import codecs
from bs4 import BeautifulSoup

urls_queue = Queue()
data_queue = Queue()
lock = threading.Lock()
f = codecs.open('out.txt', 'w', 'utf-8')
headers = {"User-Agent": "Chrome...."}

class ThreadUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        pass

class ThreadCrawl(threading.Thread):
    def __init__(self, url, queue, out_queue):
        threading.Thread.__init__(self)
        self.url = url
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        count = 5
        while count > 0:
            item = self.queue.get()
            data = self._data_post(item)
            try:
                data = urllib.parse.urlencode(data).encode('utf-8')
                req = urllib.request.Request(self.url, data=data)
                res = urllib.request.urlopen(req)
            except urllib.request.HTTPError as e:
                raise e.reason
            py_data = json.loads(res.read().decode('utf-8'))
            print(py_data)
            res.close()
            item['first'] = 'false'
            item['pn'] = item['pn'] + 1
            try:
                success = py_data['success']
                if success:
                    print("Get success...")
                else:
                    print("Get fail...")
                    time.sleep(30)
                    continue
            except Exception as e:
                print("Get Error: %s" % e)
                time.sleep(5)
                continue
            result = py_data['content']['positionResult']['result']
            if len(result) != 0:
                self.queue.put(item)
            print("now queue size is: %d" % self.queue.qsize())
            self.out_queue.put(py_data['content']['positionResult']['result'])
            self.queue.task_done()
            time.sleep(5)
            count -= 1
            print("count: %d" % count)

    def _data_post(self, item):
        pn = item['pn']
        first = 'false'
        if pn == 1:
            first = 'true'
        #return 'first=' + first + '&pn=' + str(pn) + '&kd=' + item['kd']
        return {'first': first, 'pn': str(pn), 'kd': item['kd']}

    def _item_queue(self):
        pass

class ThreadWrite(threading.Thread):
    def __init__(self, queue, lock, f):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.f = f

    def run(self):
        while True:
            item = self.queue.get()
            print("item:\r\n", item)
            self._parse_data(item)
            self.queue.task_done()

    def _parse_data(self, item):
        for i in item:
            l = self._item_to_str(i)
            with self.lock:
                print('write %s' % l)
                self.f.write(l)

    def _item_to_str(self, item):
        position_name = item['positionName']
        position_type = item['positionLables']
        work_year = item['workYear']
        education = item['education']
        job_nature = item['jobNature']
        company_name = item['companyFullName']
        company_logo = item['companyLogo']
        industry_field = item['industryLables']
        finance_stage = item['financeStage']
        company_short_name = item['companyShortName']
        city = item['city']
        salary = item['salary']
        position_first_type = item['firstType']
        create_time = item['createTime']
        position_id = item['positionId']

        ret = str(position_id) + '' + position_name + ' ' + work_year + ' ' + \
                education + ' ' + job_nature + ' ' + company_name + ' ' + \
                company_logo + ' ' + finance_stage + ' ' + \
               company_short_name + ' ' + city + ' ' + salary + ' ' + \
               position_first_type + ' ' + create_time + ' '

        return ret.join(position_type).join(' ').join(industry_field)

def main():
    for i in range(4):
        t = ThreadCrawl(
            'http://www.lagou.com/jobs/positionAjax.json', urls_queue, data_queue
        )
        t.setDaemon(True)
        t.start()
    datas = [
        {'first': 'true', 'pn': 1, 'kd': 'Java'}
    ]
    for d in datas:
        urls_queue.put(d)
    for i in range(4):
        t = ThreadWrite(data_queue, lock, f)
        t.setDaemon(True)
        t.start()

    urls_queue.join()
    data_queue.join()

    with lock:
        f.close()
    print("data_queue size: %d" % data_queue.qsize())

if __name__ == '__main__':
    main()