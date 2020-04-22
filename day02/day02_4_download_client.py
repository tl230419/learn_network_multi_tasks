'''
*****************
Date: 2020-04-22
Author: Allen
*****************
'''

import socket
import os

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(("192.168.1.102", 8080))

file_name = input("请输入文件名：\n")
tcp_client_socket.send(file_name.encode())

curr_path = os.path.dirname(__file__)
print(curr_path)
with open(curr_path + "/" + file_name, "wb") as file:
    while True:
        recv_data = tcp_client_socket.recv(1024)
        if recv_data:
            file.write(recv_data)
        else:
            break

tcp_client_socket.close()