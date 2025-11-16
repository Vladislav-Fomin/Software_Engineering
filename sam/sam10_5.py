class TooYoungError(Exception):
    """Исключение для слишком молодого возраста"""
    pass

def register_user(name, age):
    # Первое использование - регистрация на сайте
    if age < 18:
        raise TooYoungError(f"{name}, вам всего {age} лет. Регистрация с 18 лет!")
    print(f"{name} успешно зарегистрирован!")

def buy_alcohol(product, age):
    # Второе использование - покупка алкоголя
    if age < 21:
        raise TooYoungError(f"Вам {age} лет. {product} продается с 21 года!")
    print(f"Вы купили {product}")

if __name__ == "__main__":
    print("РЕГИСТРАЦИЯ НА САЙТЕ")
    try:
        register_user("Анна", 25)  #Успешно
        register_user("Иван", 16)   #Ошибка
    except TooYoungError as ex:
        print(f"{ex}")

    print("\nПОКУПКА АЛКОГОЛЯ")
    try:
        buy_alcohol("Пиво", 22)    #Успешно
        buy_alcohol("Вино", 19)    #Ошибка
    except TooYoungError as ex:
        print(f"{ex}")
