# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n=55
data = 555
def fibonachi(n, data):
    count = 2
    first = 0
    second = 1
    next = 0
    i=0
    check = False
    while i <=n:
        next = first + second
        count +=1
        if next == data:
            print(count)
            check = True
        first = second
        second = next
        next = 0
        i+=1
    if not check:
        print("-1")

    
fibonachi(n,data)