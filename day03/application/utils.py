'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

def create_http_response(status, response_body):
    '''
    :param status: 状态码
    :param response_body: 响应主体
    :return: 二进制响应报文
    '''
    response_line = "HTTP/1.1 %s \r\n" %status
    response_header = "Server:PythonWS/1.1\r\n"
    response_header += "Content-Type: text/html;charset=utf-8\r\n"
    response_blank = "\r\n"
    response_data = (response_line + response_header + response_blank).encode() + response_body

    return response_data