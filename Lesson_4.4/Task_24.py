# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.
# крч: Найти наибольшую сумму трех членов массива. Массив циклличный
from random import randint
# Вводим количество кустов
def quantity_of_bush(): 
    quantity_of_bush = randint(5, 10)
    print(f"Количество кустов: {quantity_of_bush}")
    return quantity_of_bush
# Вводим плодовитость кустов
def quantity_of_berry(quantity_of_bush):
    quantity_of_berry = [randint(1, 5) for i in range(1, quantity_of_bush)]
    print(f"Список плодовитости: {quantity_of_berry}")
    return quantity_of_berry
# Находим наибольшую плодовитость трех рядом стоищих кустов в цикличной грядке
def find_max_sum(quantity_of_berry):
    max_sum = 0
    next_1 = 0
    next_2 = 0
    for i in range(len(quantity_of_berry)):
        next_1 = i + 1
        next_2 = i + 2
        if next_2 > len(quantity_of_berry)-1 and next_1 > len(quantity_of_berry)-1:
            next_1 = 0
            next_2 = 1
        if next_2 > len(quantity_of_berry)-1:
            next_2 = 0
        if max_sum < int(quantity_of_berry[i]) +int(quantity_of_berry[next_1]) + int(quantity_of_berry[next_2]):
            max_sum = int(quantity_of_berry[i]) + int(quantity_of_berry[next_1]) + int(quantity_of_berry[next_2])
    return max_sum
    
# Выводим максимальное число ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.
print(find_max_sum(quantity_of_berry(quantity_of_bush())))

