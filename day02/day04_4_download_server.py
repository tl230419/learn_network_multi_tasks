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
    new_client_socket.close()

tcp_server_socket.close()