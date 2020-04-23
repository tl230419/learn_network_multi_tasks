'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

import socket
import re

def request_handler(new_client_socket):
    request_data = new_client_socket.recv(1024)
    if not request_data:
        print("客户端已经断开连接！")
        new_client_socket.close()
        return

    request_data_str = request_data.decode()
    request_list = request_data_str.split("\r\n")
    ret = re.search(r"\s(.*)\s", request_list[0])
    if not ret:
        print("用户请求报文格式错误！")
        new_client_socket.close()
        return

    path_info = ret.group(1)
    print("接收到用户请求：", path_info)
    if path_info == "/":
        path_info = "/index.html"

    response_header = "Server: Python-Web1.0\r\n"
    response_blank = "\r\n"

    try:
        with open("static" + path_info, "rb") as file:
            response_content = file.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_content = "Error !!! %s" % str(e)
        response_content = response_content.encode()
    else:
        response_line = "HTTP/1.1 200 OK\r\n"

    response_data = (response_line + response_header + response_blank).encode() + response_content

    new_client_socket.send(response_data)
    new_client_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)

    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("[新客户端上线]", new_client_socket)
        request_handler(new_client_socket)

if __name__ == '__main__':
        main()