'''
*****************
Date: 2020-04-19
Author: Allen
*****************
'''

import socket

#socket.socket(AddrssFamily, Type)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.close()

'''------------06--------------'''
'''
import socket

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_content = "哈哈，我来自火星！"

    send_data = send_content.encode("utf-8")

    udp_socket.sendto(send_data, ("192.168.1.102", 8080))

    udp_socket.close()
'''
'''
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

dest_addr = ('192.168.1.102', 8080)

send_data = input('请输入要发送的数据：')

udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

recv_data = udp_socket.recvfrom(1024)

print(recv_data[0].decode('gbk'))
print(recv_data[1])

udp_socket.close()
'''

'''------------08-----------'''
'''
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.1.104", 7890)
udp_socket.bind(addr)

udp_socket.sendto("hello".encode(), ("192.168.1.102", 8080))

udp_socket.close()
'''

'''------------08-2-----------'''
'''
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

local_addr = ('', 7788)
udp_socket.bind(local_addr)

recv_data = udp_socket.recvfrom(1024)

print(recv_data[0].decode('gbk'))

udp_socket.close()
'''

'''------------09-----------'''
'''
import socket

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_content = "大家好，我是渣渣辉"

    send_data = send_content.encode("utf-8")

    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

    udp_socket.sendto(send_data, ("255.255.255.255", 9090))

    udp_socket.close()
'''

'''------------11-----------'''
import socket

def send_msg(udp_socket):
    ipaddr = input("请输入接收方地址：\n")
    if len(ipaddr) == 0:
        ipaddr = "192.168.1.102"
        print("默认设置为：%s" % ipaddr)
    port = input("请输入接收方端口号：\n")
    if len(port) == 0:
        port = "6666"
        print("默认设置为：%s" % port)
    content = input("请输入要发送的内容：\n")
    udp_socket.sendto(content.encode(), (ipaddr, int(port)))

def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    re_text = recv_data[0].decode()
    print("接收到消息为：%s" % re_text)
    ip_port = recv_data[1]
    print(ip_port)

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 6666))

    while True:
        print("**************************")
        print("******* 1.发送消息 *******")
        print("******* 2.接收消息 *******")
        print("******* 3.退出系统 *******")
        print("**************************")

        num = int(input("请选择功能：\n"))
        if num == 1:
            send_msg(udp_socket)
        elif num == 2:
            recv_msg(udp_socket)
        else:
            print("程序正在退出...")
            break
            print("程序已退出！")

    udp_socket.close()