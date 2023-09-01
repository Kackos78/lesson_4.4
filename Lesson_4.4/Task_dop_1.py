# задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3, 0, -2, 0
from random import randint
def input_k():
    k = int(input("Введите какое-то натуральное число: "))
    return k
def make_coefficient(k)-> list:
    sp = []
    i = k
    while i != -1:
        sp.append(randint(-10, 10))
        i -= 1
    print(sp)
    return sp

def equation(k, sp)-> list:
    list = []
    i = 0
    count = k
    while count != 0:
        if sp[i] == 0:
            i += 1 
            count -= 1
        if sp[i] > 0 and len(list) != 0:
            list.append(f" +{sp[i]} x^{count}")
        elif count != 1:
            list.append(f" {sp[i]} x^{count}")
        else:
            list.append(f" {sp[i]} x")
        i += 1 
        count -= 1
    list.append(" = 0")
    return list

def printing_equation(list) -> print:
    print("".join(list)) 
k = input_k()
list = make_coefficient(k)
printing_equation(equation(k, list))