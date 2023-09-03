# задача 3 необязательная.

# Даны два многочлена, которые вводит пользователь. как две строки.
# Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
# решение не готово :(
import re

def input_two_str():
    first_str = input("Введите первый многочлен: ")
    second_str = input("Введите второй многочлен: ")
    return first_str, second_str

first_str, second_str = "-2x^2 + 4x + 5 = 0 ", " 5x^3 - 3*x^2 - 12 = 0"

def gruoup_str(string:str)->list:
    string_groups = re.findall(r'(\-?\s?\d*\*?x?\^?\d*\=?)', string, re.I)
    list_1=[]
    list_2 = []
    for el in string_groups:
        if el != "" and el !=" ":
            list_1.append(el)
    if list_1[0] == '-':
        list_1[1] = list_1[0]+list_1[1]
        list_1.pop(0)
    list_1.pop(-1)
    list_1.pop(-1)
    for st in list_1:
        list_2.append(st.replace(" ", ""))
        

    return list_2

def make_sum(list_1:list, list_2:list)->str:
    sum_list = []
    sum_str = ''
    for el_1 in list_1:
        for el_2 in list_2:
            first =  re.findall(r'\^\d+', el_1, re.I)
            print(f"first: {first}")
            second = re.findall(r'\^\d+', el_2, re.I)
            print(f"second: {second}")
            if first == second:
                print(True)
                argument_1 = re.findall(r'\-?\d', el_1, re.I)
                argument_2 = re.findall(r'\-?\d', el_2, re.I)
                argument_1 = "".join(argument_1)
                argument_2 = "".join(argument_2)
                sum_list.append(str(int(argument_1)+int(argument_2)).join(re.findall(r'\^?\d+', el_1, re.I)))
                
    
    sum_str = sum_list
    return sum_str

string_groups_1 = gruoup_str(first_str)
string_groups_2 = gruoup_str(second_str)
ansver = make_sum(string_groups_1, string_groups_2)
print(ansver)
# print(string_groups_1, string_groups_2)