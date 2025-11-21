def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = 200
fib_gen = fib(n)
for i in range(n):
    result = next(fib_gen)
print(result)
#Написан генератор чисел фибоначчи с использованием yield и иттератора next

