# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


list1 = [0, -1, 5, 2, 3]
num = int(0)
temp = int(list1[0])
for el in range(len(list1)):
    if list1[el] > temp:
        num += 1
    temp = list1[el]
print(num)