'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(("www.hupu.com", 80))

request_line = "GET / HTTP/1.1\r\n"

request_header = "Host: www.hupu.com\r\n"
request_data = request_line + request_header + "\r\n"

tcp_socket.send(request_data.encode())

response_data = tcp_socket.recv(4096)
response_str_data = response_data.decode()
print(response_str_data)

index = response_str_data.find("\r\n\r\n")
html_data = response_str_data[index+4:]

with open("index.html", "wb") as file:
    file.write(html_data.encode())

tcp_socket.close()