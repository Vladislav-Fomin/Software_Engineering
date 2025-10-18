def numpad_master(str):
    digit_count = {}

    for el in str:
        digit = int(el)
        digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))
    top_three = sorted_digits[:3]
    return dict(top_three)
def print_numpad_master(res):
    print("Топ-3 самых частых цифр (в порядке возрастания ключа): ")
    for digit in sorted(res.keys()):
        print(f"Цифра {digit}, Количетсво {res[digit]} ")

test1 = "121113456789012345678901234567890"
test2 = "765432121456732345678909876543345678909876"

res1 = numpad_master(test1)
res2 = numpad_master(test2)

print_numpad_master(res1)
print_numpad_master(res2)

