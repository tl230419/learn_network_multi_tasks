'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import socket
import threading

def send_data(udp_socket):
    send_content = input("请输入要发送的内容：")
    ip_addr = input("请输入IP地址，格式为：xxx.xxx.xxx.xxx :")
    port = int(input("请输入端口号："))

    data = send_content.encode("utf-8")
    udp_socket.sendto(data, (ip_addr, port))

def recv_data(udp_socket):
    while True:
        data = udp_socket.recvfrom(1024)
        if data:
            msg, list_port = data
            msg = msg.decode("gbk")
            print(msg, list_port)
        else:
            break

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7878))

    t1 = threading.Thread(target=recv_data, args=(udp_socket,))
    t1.setDaemon(True)
    t1.start()

    while True:
        print("----------------------------------------")
        print("--------------1.发送数据-----------------")
        print("--------------2.退出系统-----------------")
        print("-----------------------------------------")

        num = int(input("请选择功能【1/2】:"))
        if num < 1 or num > 3:
            print("输入不合法，请重新输入")
        else:
            if num == 1:
                send_data(udp_socket)
            elif num == 2:
                print("正在退出系统")
                print("系统已退出")
                break

if __name__ == '__main__':
    main()