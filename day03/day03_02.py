'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

import socket

def request_handler(new_client_socket):
    request_data = new_client_socket.recv(1024)
    if not request_data:
        print("客户端已经断开连接！")
        new_client_socket.close()
        return

    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server: Python-Web1.0\r\n"
    response_blank = "\r\n"
    response_content = "Hello World!"
    response_data = response_line + response_header + response_blank + response_content

    new_client_socket.send(response_data.encode())
    new_client_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)

    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("[新客户端上线]", new_client_socket)
        request_handler(new_client_socket)

if __name__ == '__main__':
        main()