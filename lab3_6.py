str = 'Привет всем изучающим Python!'
value = input()
for i in str:
    if i == value:
        index = str.find(value)
        print(f"Буква '{value}' есть в сторке под {index} индексом")
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")