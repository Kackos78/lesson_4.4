# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def Input_nums()-> list:
    n = None
    m = None
    while n == None:
        try: 
            n = int(input("Введите число N: "))
        except:
            n = None
            print("Ошибка ввода") 
    
    while m == None:
        try: m = int(input("Введите число M: "))
        except:
            print("Ошибка ввода") 
            m = None
    list_1 = []
    list_2 = []
    while len(list_1) < n:
        list_1.append(int(input("Введите следущее число в списке N: ")))
    while len(list_2) < m:
        list_2.append(int(input("Введите следущее число в списке M: ")))
    
    returned_list = list_1+ list_2
    print(returned_list)
    return(returned_list)

def Make_set(list)-> set: 
    returned_list = set(list)
    print(returned_list)
    return returned_list

def SortGrow(list_set)->list:
    list_set = list(list_set)
    list_set.sort()
    print(list_set)
    return list_set

SortGrow(Make_set(Input_nums()))

