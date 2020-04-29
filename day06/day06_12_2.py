'''
*****************
Date: 2020-04-28
Author: Allen
*****************
'''

from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()

def my_download(file_name, url):
    print("GET: %s" % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as f:
        f.write(data)

    print("%d bytes received from %s." % (len(data), url))

gevent.joinall([
    gevent.spawn(my_download, "1.mp4", "https://pan.baidu.com/play/video#/video?path=%2Fslam%2F79-%E9%AB%98%E6%96%AF%E8%BF%87%E7%A8%8B%E5%9C%A8%E8%BF%9E%E7%BB%AD%E6%97%B6%E9%97%B4SLAM%E4%B8%8E%E8%BF%90%E5%8A%A8%E8%A7%84%E5%88%92%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8%20-%20%E8%91%A3%E9%9D%96%2F_2017-0621-2001-08%20(online-video-cutter.com).mp4"),
    #gevent.spawn(my_download, "2.mp4", "http://oo52bgdsl.bkt.clouddn.com/05day-03-%E3%80%90%E6%8E%8C%E6%8F%A1%E3%80%91%E6%97%A0%E5%8F%82%E6%95%B0%E6%97%A0%E8%BF%94%E5%9B%9E%E5%80%BC%E5%87%BD%E6%95%B0%E7%9A%84%E5%AE%9A%E4%B9%89%E3%80%81%E8%B0%83%E7%94%A8%28%E4%B8%8B%29.mp4")
])