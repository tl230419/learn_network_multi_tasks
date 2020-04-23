'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

import socket
from application import app

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

        response_data = app.application(request_data)
        new_client_socket.send(response_data)
        new_client_socket.close()


def main():
    ws = WebServer()
    ws.start()

if __name__ == '__main__':
    main()