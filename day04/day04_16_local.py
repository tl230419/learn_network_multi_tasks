'''
*****************
Date: 2020-04-25
Author: Allen
*****************
'''

import threading

local_class = threading.local()

def show_score():
    name = local_class.student
    score = local_class.score
    print("Hello {}, 总分为 {}".format(name, score))

def handle_student(name, score):
    local_class.student = name
    local_class.score = score
    show_score()

t1 = threading.Thread(target=handle_student, args=("赵四", 80))
t2 = threading.Thread(target=handle_student, args=("刘能", 99))

t1.start()
t2.start()
t1.join()
t2.join()

