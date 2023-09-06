#  В списке хранятся числа. Ножно выюрать только четные числа и составит список пар число-крадрат


arr = [1,2,3,6,6,6,5,8,4,7,45,8,4,4,54,647,54]

def math(op, x):
    return op(x)

def pow(arr):
    arr_done = []
    for i in arr:
        arr_done.append(f'{i} - {i**2}')
    return arr_done


print(pow([x for x in arr if x % 2 == 0]))
