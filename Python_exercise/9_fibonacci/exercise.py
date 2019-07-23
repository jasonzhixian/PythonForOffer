def fibonacci(n):
    a, b = 0, 1
    for i in range(n): 
        yield a
        a, b = b, a + b

s = fibonacci(10)
for j in s:
    print(j, end = ' ')
