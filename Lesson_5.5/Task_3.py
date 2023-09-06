# Задача 1 необязательная. Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

#  Так я устал, дань, попробуй на выходных это решить всеткаи через дерево, должно быть сильно проще чем тот вариант что ты пишешь

import re
arifm = " 2*2+3+3*4+4 "

def calculation(arr:list):
    if re.findall(r'\*',arifm, re.I):
        for el in arr:
            return el.pop(0) * el.pop(-1)


def re_str(arifm: str)-> int:
    arifm = arifm.replace(' ', '')
    multiplication = re.findall(r'\d+\*\d+',arifm, re.I)
    division = re.findall(r'\d+\\\d+',arifm, re.I)
    sum = re.findall(r'\d+\+\d+',arifm, re.I)
    subtraction = re.findall(r'\d+\-\d+',arifm, re.I)

    # return 