'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import select
import time
import socket
import sys
import re
import multiprocessing

class WSGI_Server(object):
    def __init__(self, port, documents_root, app):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server_socket.bind(("", port))
        self.server_socket.listen(128)

        # Set resources file path
        self.documents_root = documents_root
        # set function(object) for web frame call
        self.app = app

        self.headers = []

    def run_forever(self):
        while True:
            new_socket, new_addr = self.server_socket.accept()
            new_socket.settimeout(3) # 3s
            # Create a new process to finish client request task
            new_process = multiprocessing.Process(target=self.deal_with_request, args=(new_socket,))
            new_process.start()
            new_socket.close()

    def deal_with_request(self, client_socket):
        while True:
            try:
                request = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("=========>", ret)
                client_socket.close()
                return

            # Judge explorer whether close
            if not request:
                client_socket.close()
                return

            request_lines = request.splitlines()
            print("request line:\r\n")
            for i, line in enumerate(request_lines):
                print(i, line)

            # Get request file(index.html)
            # GET /a/b/c/d/e/index.html HTTP/1.1
            ret = re.match(r"([^/])*([^ ]+)", request_lines[0])
            if ret:
                print("正则提取数据：", ret.group(1))
                print("正则提取数据：", ret.group(1))
                file_name = ret.group(2)
                if file_name == "/":
                    file_name = "/index.html"

            # If file not end with py, as regular file
            if not file_name.endswith(".py"):
                try:
                    f = open(self.documents_root+file_name, "rb")
                except:
                    response_body = "file not found, 请输入正确的url"

                    response_header = "HTTP/1.1 404 not found\r\n"
                    response_header += "Content-Type: text/html;charset=utf-8\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))

                    response = response_header + response_body

                    # Return header to explorer
                    client_socket.send(response.encode('utf-8'))
                else:
                    content = f.read()
                    f.close()

                    response_body = content

                    response_header = "HTTP/1.1 200 OK\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    # Return header to explorer
                    client_socket.send(response_header.encode('utf-8') + response_body)
            # End with py file, as dynamic page
            else:
                # Store data that pass to web frame
                env = dict()
                env['PATH_INFO'] = file_name

                # Store web return data
                response_body = self.app(env, self.set_response_headers)

                # Combinate header and body
                response_header = "HTTP/1.1 {status}\r\n".format(status=self.headers[0])
                response_header += "Content-Type: text/html;charset=utf-8\r\n"
                response_header += "Content-Length: %d\r\n" % (len(response_body))
                for temp_header in self.headers[1]:
                    response_header += "{0}:{1}\r\n".format(*temp_header)

                response = response_header + "\r\n"
                response += response_body

                client_socket.send(response.encode('utf-8'))

    def set_response_headers(self, status, headers):
        response_header_default = [
            ("Data", time.ctime()),
            ("Server", "Allen-python mini web server")
        ]

        self.headers = [status, response_header_default + headers]

g_static_document_root = "./static"
g_dynamic_document_root = "./dynamic"

def main():
    if len(sys.argv) == 3:
        port = sys.argv[1]
        if not port.isdigit():
            print("端口不是数字")
            return
        port = int(port)
        web_frame_module_app_name = sys.argv[2]
    else:
        print("运行方式：python3 xxx.py 7890 my_web_frame_name:application")
        return

    print("http服务器使用的port:%s" % port)

    sys.path.append(g_dynamic_document_root)

    ret = re.match(r"([^:]*):(.*)", web_frame_module_app_name)
    if ret:
        web_frame_module_name = ret.group(1)
        app_name = ret.group(2)

    web_frame_module = __import__(web_frame_module_name)
    app = getattr(web_frame_module, app_name)

    http_server = WSGI_Server(port, g_static_document_root, app)
    http_server.run_forever()

if __name__ == '__main__':
    main()