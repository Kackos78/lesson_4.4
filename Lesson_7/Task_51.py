# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:                                     Вывод:
# values = [0, 2, 10, 6]                    same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# same_by(lambda x: x % 2, values):
def same_by(characteristic, objects):
    # same_or_not = list(map(characteristic, objects))
    # for i in range(len(same_or_not)-1):
    #     if same_or_not[i] != same_or_not[i+1]:
    #         return False
    # return True
    S = set(list(map(characteristic, objects)))
    if len(S) <= 1:
        return True
    else:
        return False


values = [0, 2, 10, 6,] 

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')