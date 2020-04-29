'''
*****************
Date: 2020-04-28
Author: Allen
*****************
'''

from gevent import monkey
import urllib.request
import gevent

monkey.patch_all()

def download_img(img_url, filename):
    try:
        response = urllib.request.urlopen(img_url)
        with open(filename, "wb") as img_file:
            while True:
                img_data = response.read(1024)
                if img_data:
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print("文件 %s 下载失败！%s" % (filename, str(e)))
    else:
        print("图片 %s 下载完成！" % filename)

def main():
    img_url1 = "http://img.mp.itc.cn/upload/20170716/8e1b835f198242caa85034f6391bc27f.jpg"
    img_url2 = "http://img.mp.sohu.com/upload/20170529/d988a3d940ce40fa98ebb7fd9d822fe2.png"
    img_url3 = "http://image.uczzd.cn/11867042470350090334.gif?id=0&from=export"

    gevent.joinall([
        gevent.spawn(download_img, img_url1, "1.gif"),
        gevent.spawn(download_img, img_url2, "2.gif"),
        gevent.spawn(download_img, img_url3, "3.gif")
    ])

if __name__ == '__main__':
    main()