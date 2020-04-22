'''
*****************
Date: 2020-04-22
Author: Allen
*****************
'''

import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_server_socket.bind(("", 8080))
tcp_server_socket.listen(128)

while True:
    new_client_socket, ip_port = tcp_server_socket.accept()
    print(ip_port)
    recv_data = new_client_socket.recv(1024)
    file_name = recv_data.decode()
    print(file_name)
    try:
        with open(file_name, "rb") as file:
            while True:
                file_data = file.read(1024)
                if file_data:
                    new_client_socket.send(file_data)
                else:
                    break
    except:
        print("文件 %s 下载出错" % file_name)
    else:
        print("文件 %s 下载成功" % file_name)
    new_client_socket.close()

tcp_server_socket.close()