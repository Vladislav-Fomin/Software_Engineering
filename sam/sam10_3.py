def add_two():
    try:
        inputs = input("Введите число: ")
        number = float(inputs)
        result = 2 + number
        print(f"2 + {number} = {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


if __name__ == '__main__':
    print("Тест 1 (корректный ввод):")
    add_two()

    print("\nТест 2 (строка):")
    add_two()

    print("\nТест 3 (дробное число):")
    add_two()

    print("\nТест 4 (специальные символы):")
    add_two()
