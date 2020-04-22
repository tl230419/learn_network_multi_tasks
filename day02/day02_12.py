import socket

# 判断模块是否是程序的入口，判断整个模块是否是主模块
if __name__ == '__main__':

    # 创建socket
    # AF_INET 表示ip地址，也是internet互联网
    # SOCK_DGRAM 表示使用udp 协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_content = "hello"

    send_data = send_content.encode("utf-8")

    # 绑定端口
    # udp_socket.bind(("", 4545))

    udp_socket.sendto(send_data, ("192.168.1.100", 8082))

    # 接收数据
    recv_data = udp_socket.recvfrom(1024)

    # 打印接收的数据
    print(recv_data[0].decode("gbk"))

    # 关闭套接字
    udp_socket.close()