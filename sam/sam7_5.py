import datetime

def show_diary():
    with open('diary.txt', 'r', encoding='utf-8') as file:
        entries = file.readlines()

    print("\nМОЙ ДНЕВНИК")
    for i, entry in enumerate(entries, 1):
        parts = entry.strip().split('|')
        if len(parts) == 4:
            date, mood, text, tag = parts
            if tag:
                print(f"{i}. {date} [{tag}] - {text} (настроение: {mood}/5)")
            else:
                print(f"{i}. {date} - {text} (настроение: {mood}/5)")
        else:  # Старый формат без тега
            date, mood, text = parts[0], parts[1], ' '.join(parts[2:])
            print(f"{i}. {date} - {text} (настроение: {mood}/5)")

def add_entry():
    print("\nНОВАЯ ЗАПИСЬ")
    date = input("Дата (дд.мм.гггг или Enter для сегодня): ")
    if not date:
        date = datetime.datetime.now().strftime("%d.%m.%Y")

    mood = input("Настроение (1-5): ")
    text = input("Опишите ваш день: ")
    tag = input("Добавить тег (Enter чтобы пропустить): ")

    with open('diary.txt', 'a', encoding='utf-8') as file:
        file.write(f"{date}|{mood}|{text}|{tag}\n")

    print("Запись добавлена!")

def search_entries():
    with open('diary.txt', 'r', encoding='utf-8') as file:
        entries = file.readlines()

    print("\n1 - Поиск по тексту")
    print("2 - Поиск по тегу")
    choice = input("Выберите тип поиска: ")

    if choice == '1':
        keyword = input("Поиск по тексту: ").lower()
    elif choice == '2':
        keyword = input("Поиск по тегу: ").lower()
    else:
        print("Неверный выбор!")
        return

    print("\nРЕЗУЛЬТАТЫ ПОИСКА:")
    for entry in entries:
        if keyword in entry.lower():
            parts = entry.strip().split('|')
            if len(parts) == 4:
                date, mood, text, tag = parts
                if tag:
                    print(f"{date} [{tag}] - {text}")
                else:
                    print(f"{date} - {text}")
            else:
                date, mood, text = parts[0], parts[1], ' '.join(parts[2:])
                print(f"{date} - {text}")

while True:
    print("\n1 - Показать дневник")
    print("2 - Добавить запись")
    print("3 - Поиск")
    print("4 - Выйти")

    choice = input("Выберите: ")

    if choice == '1':
        show_diary()
    elif choice == '2':
        add_entry()
    elif choice == '3':
        search_entries()
    elif choice == '4':
        break
