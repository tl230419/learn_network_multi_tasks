
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num
    return "done"

F = fib(5)
value = next(F)
print("111->", value)

def fibonacci(n):
    #a = 0
    a = 1
    b = 1

    curr_index = 0
    print("-------------111-------------")

    while curr_index < n:
        result = a
        a, b = b, a
        curr_index += 1
        print("----------222------------")
        yield result
        print("----------333------------")
        return "我是return的内容"

fib = fibonacci(5)

value = next(fib)
print("222", value)

try:
    value = next(fib)
    print("333", value)
except StopIteration as e:
    print("return信息：%s" % e.value)