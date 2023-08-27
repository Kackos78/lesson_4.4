# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному
# числу k и вывести его.


# list_1 = [1, 2, 3, 4, 5]
# k = 6
list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 8
less = list_1[0]
more = list_1[0]
bigger = list_1[0]
chek = False
for el in list_1:
    if el == k:
        chek = True
        print(el)
    elif el > less and el < k:
        less = el
    elif el > bigger and el > k:
        bigger = el
for el in list_1:
    if el < bigger and el > k:
        more = el
if not chek:
    if less < more:
        if k - less < more - k:
            print(less)
        if more - k < k - less:
            print(more)
    else: print(less)