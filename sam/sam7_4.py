def readFile(file):
    with open(file, 'r') as f:
        text = f.read().strip()
        words = text.split()
    return words
def censor_text(text, forbidden_words):
    new_text = []
    i = 0
    while i < len(text):
        found = False
        for word in forbidden_words:
            forbidden_lower = word.lower()
            if i + len(word) <= len(text):
                substring = text[i:i + len(word)].lower()
                if substring == forbidden_lower:
                    new_text.append('*' * len(word))
                    i += len(word)
                    found = True
                    break
        if not found:
            new_text.append(text[i])
            i += 1

    return ''.join(new_text)

forbidden_words = readFile('sam7_4.txt')
print("Запрещенные слова:", forbidden_words)
text = input("Введите предложение: ")
censored_text = censor_text(text, forbidden_words)
print(f"Результат после цензуры: {censored_text}")

