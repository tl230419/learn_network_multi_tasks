

def fibonacci(n):
    a = 0
    b = 1

    curr_index = 0

    while curr_index < n:
        result = a
        a, b = b, a
        curr_index += 1
        print("----------222------------")
        param = yield result
        print("send------------", param)
        #return

fib = fibonacci(5)
value = fib.send(None)
print(value)

value = fib.send("abc")
print(value)

value = fib.send("def")
print(value)