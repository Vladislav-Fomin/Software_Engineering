def readFile(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = [line.strip() for line in f]
    return text

def updateFile(file):
    new_text = input("Введите новые данные: ")
    with open(file, 'a', encoding='utf-8') as f:
        f.write(new_text + '\n')
    return readFile(file)

while True:
    print('1 - Посмотреть файл')
    print('2 - Добавить данные')
    print('3 - Выход')
    choice = input("Выберите действие: ")
    if choice == '1':
        print(readFile('sam7_2.txt'))
    elif choice == '2':
        print(updateFile('sam7_2.txt'))
    elif choice == '3':
        break
    else:
        print("Неверный выбор")

