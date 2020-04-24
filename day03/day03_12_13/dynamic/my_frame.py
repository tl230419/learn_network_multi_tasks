'''
*****************
Date: 2020-04-24
Author: Allen
*****************
'''

import time

templates_root = "./templates"

def index(file_name):
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(templates_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()
        return content

def center(file_name):
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(templates_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()
        return content

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    if file_name == "/index.py":
        return index(file_name)
    elif file_name == "/center.py":
        return center(file_name)
    else:
        return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()