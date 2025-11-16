def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("Файл пустой")
            print(content)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    print("Проверка пустого файла:")
    read_file('empty.txt')

    print("Проверка файла с данными:")
    read_file('full.txt')

    print("Проверка несуществующего файла:")
    read_file('none.txt')
