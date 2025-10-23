def file_statistics(file):
    with open(file, 'r') as f:
        text = f.read()

    letter_count = 0
    for char in text:
        if char.isalpha():
            letter_count += 1
    word_count = len(text.split())
    line_count = text.count('\n') + 1 if text else 0

    print('Статистика файла:')
    print(letter_count, 'букв')
    print(word_count, 'слов')
    print(line_count, 'строк')

file_statistics('test.txt')
