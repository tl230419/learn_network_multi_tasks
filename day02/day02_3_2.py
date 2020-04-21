'''
*****************
Date: 2020-04-22
Author: Allen
*****************
'''

from socket import *
import platform

tcp_server_socket = socket(AF_INET, SOCK_STREAM)
address = ('192.168.1.102', 7788)
tcp_server_socket.bind(address)
tcp_server_socket.listen(128)

sysstr = platform.system()
while True:
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("已经连接客户端：", ip_port)
    while True:
        recv_data = new_client_socket.recv(1024)
        if recv_data:
            if sysstr == "Windows":
                print('-----------------------------------')
                print("收到数据：", recv_data.decode("gbk"))
            elif sysstr == "Linux":
                print('-----------------------------------')
                print("收到数据：", recv_data.decode("utf-8"))
        else:
            break
        new_client_socket.send("好的，已经收到！".encode('gbk'))
    new_client_socket.close()
tcp_server_socket.close()