# задача 2 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def input_num()->int: 
    num = int(input("Введите целое число: ")) 
    return num

def make_bin(num: int)-> int:
    ansver = ''
    while num != 0:
        ansver = ansver + str(num % 2)
        num = num // 2
    ansver = ''.join(reversed(ansver))
    return '0b' + ansver

def make_oct(num: int)->int:
    if num == 0:
        return '0o'
    else:
        res = str(num % 8)
        return str(make_oct(num // 8)) + res
    
num = input_num()

print(make_bin(num))
print(make_oct(num))
print(bin(num))
print(oct(num))