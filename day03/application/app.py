'''
*****************
Date: 2020-04-23
Author: Allen
*****************
'''

from application import utils

def parse_request(request_data):
    request_text = request_data.decode()
    request_list = request_text.split("\r\n")
    request_line_parts = request_list[0].split(" ")

    request_line_dict = dict()
    request_line_dict['file_path'] = request_line_parts[1]
    request_line_dict['version'] = request_line_parts[2]
    request_line_dict['method'] = request_line_parts[0]

    if request_line_dict['file_path'] == "/":
        request_line_dict['file_path'] = "/index.html"

    return request_line_dict

def application(request_data):
    request_line_dict = parse_request(request_data)
    print(request_line_dict)

    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:PythonWS/1.1\r\n"
    response_header += "Content-Type: text/html;charset=utf-8\r\n"
    response_blank = "\r\n"
    path_info = "static" + request_line_dict['file_path']

    try:
        with open(path_info, "rb") as file:
            response_body = file.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = "Error !! %s" % str(e)
        response_body = response_body.encode()

    response_data = (response_line + response_header + response_blank).encode() + response_body

    return response_data

def application(curr_dir, request_data):
    request_line_dict = parse_request(request_data)
    path_info = curr_dir + request_line_dict['file_path']

    try:
        with open(path_info, "rb") as file:
            response_body = file.read()
            response_data = utils.create_http_response("200 OK", response_body)
    except Exception as e:
        response_body = "Error !! %s" % str(e)
        response_body = response_body.encode()
        response_data = utils.create_http_response("404 Not Found", response_body)

    return response_data