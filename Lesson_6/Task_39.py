# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
from random import randint


N = int(input("Введите длинну первого массива: "))
list_N = [randint(1,10) for _ in range(N)]
M = int(input("Введите длинну второго массива: "))
list_M = [randint(1,10) for _ in range(M)]

print(list_N)
print(list_M)

print([x for x in list_N if x not in set(list_M) ])
