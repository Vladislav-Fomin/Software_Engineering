def office_entries(tpl, id):
    if id not in tpl:
        return ()

    index1 = tpl.index(id)
    count_index = []

    for i in range(len(tpl)):
        if tpl[i] == id:
            count_index.append(i)

    if len(count_index) >= 2:
        index2 = count_index[1]
        return tpl[index1: index2 + 1]
    else:
        return tpl[index1:]

print(office_entries((1,2,3), 8))
print(office_entries((1,8,3,4,8,8,9,2), 8))
print(office_entries((1,2,8,5,1,2,9), 8))
