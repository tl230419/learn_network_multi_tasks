# 导入模块
import socket

# 创建套接字
tcp_click_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立TCP连接
tcp_click_socket.connect(("192.168.1.104", 6666))

# 定义要发送的内容
send_content = "hi,I'm weige !"

# 对发送的内容进行转码
send_data = send_content.encode("utf-8")

# 发送数据
tcp_click_socket.send(send_data, )

# 关闭连接
tcp_click_socket.close()