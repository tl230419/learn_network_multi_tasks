'''
*****************
Date: 2020-04-22
Author: Allen
*****************
'''

import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(("192.168.1.102", 7878))
tcp_client_socket.send("哈哈哈，打不过我吧？！".encode("utf-8"))

recv_data = tcp_client_socket.recv(1024)
# Chinese can not use utf-8 format decode!!!
print("接收到数据：", recv_data.decode("gbk"))

tcp_client_socket.close()