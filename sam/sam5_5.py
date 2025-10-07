def name(lst):
    result_set = set()
    for num in set(lst):
        count = lst.count(num)
        result_set.add(num)
        if count > 1:
            for i in range(2, count + 1):
                result_set.add(str(num) * i)

    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(f"Первый список: {list_1} После изменений: {name(list_1)}\n"
      f"Первый список: {list_2} После изменений: {name(list_2)}\n"
      f"Первый список: {list_3} После изменений: {name(list_3)}\n")
