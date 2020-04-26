'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

class Fibonacci():
    def __init__(self, num):
        self.num = num
        self.a = 1
        self.b = 1

        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.num:
            result = self.a
            #print("a:", result)
            #print("before-->", self.a, self.b)
            self.a, self.b = self.b, self.a + self.b
            #print("<--after-->", self.a, self.b)
            self.current_index += 1
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    fib_iterator = Fibonacci(5)
    i = 0
    for value in fib_iterator:
        print(value, end=" ")
        #print("index: ", i)
        i += 1
    print("\r\n")

    li = list(Fibonacci(15))
    print(li)
    tp = tuple(Fibonacci(6))
    print(tp)