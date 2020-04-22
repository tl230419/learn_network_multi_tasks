'''
*****************
Date: 2020-04-22
Author: Allen
*****************
'''

import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(("192.168.1.102", 8080))

file_name = input("请输入文件名：\n")
tcp_client_socket.send(file_name.encode())
tcp_client_socket.close()