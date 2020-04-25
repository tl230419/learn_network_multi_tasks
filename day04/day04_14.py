'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import socket
import threading

def recv_msg(new_socket):
    while True:
        recv_data = new_socket.recv(1024)
        if recv_data:
            re_text = recv_data.decode("gbk")
            print(re_text)
        else:
            break

        new_socket.send("7878收到，谢谢！".encode("utf-8"))
    new_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 7878))
    tcp_server_socket.listen(128)

    while True:
        new_socket, ip_port =tcp_server_socket.accept()
        print(ip_port)

        t1 = threading.Thread(target=recv_msg, args=(new_socket,))
        t1.setDaemon(True)
        t1.start()

    tcp_server_socket.close()

if __name__ == '__main__':
    main()