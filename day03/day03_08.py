'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

import socket
from application import app
import sys

class WebServer(object):
    def __init__(self, port):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

        self.projects_dict = dict()
        self.current_dir = ""
        self.projects_dict['植物大战僵尸-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物大战僵尸-外挂版'] = "zwdzjs-v2"
        self.projects_dict['保卫萝卜'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读心术'] = "dxs"

        self.init_projects()

    def init_projects(self):
        dict_keys = tuple(self.projects_dict.keys())
        print("请选择要发布的项目：\r\n")
        for index, value in enumerate(dict_keys):
            print("%d.%s" % (index, value))

        sel_num = int(input("请选择要发布的游戏编号：\n"))
        sel_key = dict_keys[sel_num]
        print("已经成功发布游戏[%s]，客户端请刷新网页使用！" % sel_key)

        self.current_dir = self.projects_dict[sel_key]

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

        response_data = app.application(self.current_dir, request_data)
        new_client_socket.send(response_data)
        new_client_socket.close()


def main():
    if len(sys.argv) != 2:
        print("启动失败，参数个数错误！正确格式：python xxx.py 8080")
        return

    if not sys.argv[1].isdigit():
        print("启动失败，端口不是数字")
        return

    port = int(sys.argv[1])

    ws = WebServer(port)
    ws.start()

if __name__ == '__main__':
    main()