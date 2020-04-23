'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

import socket

class WebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 8080))
        tcp_server_socket.listen(128)

        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            self.request_handler(new_client_socket, ip_port)

    def request_handler(self, new_client_socket, ip_port):
        request_data = new_client_socket.recv(1024)
        if not request_data:
            print("客户端[%s]已经下线" % str(ip_port))
            new_client_socket.close()
            return

        request_text = request_data.decode()
        request_list = request_text.split("\r\n")
        request_line_parts = request_list[0].split(" ")
        file_path = request_line_parts[1]

        if file_path == "/":
            file_path = "/index.html"

        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server:PythonWS/1.1\r\n"
        response_header += "Content-Type: text/html;charset=utf-8\r\n"
        response_blank = "\r\n"
        path_info = "static" + file_path

        try:
            with open(path_info, "rb") as file:
                response_body = file.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_body = "Error !! %s" % str(e)
            response_body = response_body.encode()

        response_data = (response_line + response_header + response_blank).encode() + response_body
        new_client_socket.send(response_data)
        new_client_socket.close()


def main():
    ws = WebServer()
    ws.start()

if __name__ == '__main__':
    main()