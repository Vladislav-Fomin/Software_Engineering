def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = 200
fib_gen = fib(n)

with open('fib.txt', 'w') as file:
    for i in range(n):
        result = next(fib_gen)
        file.write(f"{result}\n")
        if i == n - 1:
            print(result)

#К прошлой задаче добавлена запись каждого числа в файл