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
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.1.104", 7890)
udp_socket.bind(addr)

udp_socket.sendto("hello".encode(), ("192.168.1.102", 8080))

udp_socket.close()