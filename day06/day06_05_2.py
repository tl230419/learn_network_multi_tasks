'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

L = [x*2 for x in range(5)]
print(L)

G = (x*2 for x in range(5))
print(G)

print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

#print(next(G))

G1 = (x*2 for x in range(5))
for x in G1:
    print(x)

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

fib = fibonacci(5)

value = next(fib)
print(value)

value = next(fib)
print(value)