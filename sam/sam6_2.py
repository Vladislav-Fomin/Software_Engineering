def delEl_tuple(tpl, num):
    list_tpl = list(tpl)
    if num in list_tpl:
        list_tpl.remove(num)
    return tuple(list_tpl)

test1 = delEl_tuple((1,2,3), 1)
test2 = delEl_tuple((1,2,3,1,2,3,4,5,2,3,4,2,4,2), 3)
test3 = delEl_tuple((2,4,6,6,4,2), 9)
print(test1)
print(test2)
print(test3)

