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

client_socket, ip_port = tcp_server_socket.accept()
print("已经连接客户端：", ip_port)

recv_data = client_socket.recv(1024)
sysstr = platform.system()
if sysstr == "Windows":
    print("收到数据：", recv_data.decode("gbk"))
elif sysstr == "Linux":
    print("收到数据：", recv_data.decode("utf-8"))

client_socket.send("好的，已经收到！".encode('gbk'))
client_socket.close()
tcp_server_socket.close()