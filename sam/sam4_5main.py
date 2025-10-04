from sam4_5dop import heron_area

if __name__ == "__main__":
    print("Введите длины сторон треугольника")
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))

    result = heron_area(a, b, c)

    if result is None:
        print("Треугольник с такими сторонами не существует")
    else:
        print(f"Площадь треугольника = {result}")

#В задаче были применены: импорт файла, функция, вспоминили формулу Герона)