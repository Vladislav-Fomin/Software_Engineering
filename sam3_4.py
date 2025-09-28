str = input('Введите предложение на латинице: ')
glas = 'aeiou'
count = 0
#Поиск длины предложения
print('Длина предложения:', len(str))
#Вывод предлложения в нижнем регистре
print(f"Предложение в нижнем регистре: {str.lower()}")
#Подсчет гласных букв
for i in str:
    if i in glas:
        count += 1
print("Количество гласных букв = ", count)
#Замена слов
if 'ugly' in str:
    print("Замена слов:", str.replace('ugly', 'beauty'))
else:
    print("Заменять нечего")
#Проверка условия
if(str[:3] == 'The') and (str[len(str)-3:] == 'end'):
    print("Условие выполнено")
else:
    print("Условие невыполнено")