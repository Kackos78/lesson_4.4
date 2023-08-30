def Summa(num1: int, num2: int) -> int:
    if not isinstance(num1, int):
        raise ValueError("This must be a integer")
    return num1 + num2

print(Summa(1,3))
print(Summa("Hi", " all "))