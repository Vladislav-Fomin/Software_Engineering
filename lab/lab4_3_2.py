def main(one, two):
    return one + two

for i in range(5):
    answer = main(one = 1, two = 5)
    print(answer)
#Альтернативное решение предыдущей задачи, но уже с передачей аргументов сразу в вызове функции