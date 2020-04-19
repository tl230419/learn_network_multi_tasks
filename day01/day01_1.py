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
import socket

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_content = "哈哈，我来自火星！"

    send_data = send_content.encode("utf-8")

    udp_socket.sendto(send_data, ("192.168.1.102", 8080))

    socket.close()