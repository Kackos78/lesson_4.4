num = int(input("Введите число: "))
# print(num)
i = 0
# while i < num:
#     print(f"Квадрат числа {i} равен {i**2}")
#     i += 1

for u in range (num+1):
    print(f"Квадрат числа {i} равен {i**2}")
    if i % 2 == 1:
        print("Нечетное")
    elif i % 3 == 0:
        print("Делится на три")