from random import randint
def kubik():
    value = randint(1,6)
    print(f"Выпало: {value}")
    if value == 5 or value == 6:
        print("Вы победили")
    elif value == 1 or value == 2:
        print("Вы проиграли")
    else:
        kubik()

if __name__ == '__main__':
    kubik()

#Изучение рекурсивных функций и применение на практике для решения задачи + изучение модуля random