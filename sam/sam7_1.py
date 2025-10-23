with open('article.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
count_words = len(words)
cleaned_words = []
for word in words:
    cleaned_word = word.strip('.,!?;:"()[]{}«»—_- \n\t')
    cleaned_word = cleaned_word.lower()
    if cleaned_word:
        cleaned_words.append(cleaned_word)

word_frequency = {}
for word in cleaned_words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

most_word = None
max = 0

for word, count in word_frequency.items():
    if count > max:
        max = count
        most_word = word

print(f"Количество слов - {count_words}")

if most_word:
    print(f"\nСамое частое слово: '{most_word}'")
    print(f"Количество повторений: {max}")
