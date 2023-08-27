sp = [55, 44, "hello", True, 99.88, 100]

# for i in range(len(sp)):
#     print(sp[i])

# for item in sp:
#     print(item )

# for i, value in enumerate(sp):
#     print(i, value)

# 
# print("hello" in sp)

# sp.append("last")
# sp.insert(0, "zero")
# sp.extend([1,2,3])
# sp+=[1,2,3] * 3
# print([None]*10)
# del sp[0]
# sp.remove(True) # только первое по списку такое значение
# a = sp.pop() # Вырезать

# print(a)
# print(sp)
# print(len(sp))

# list tuple set dict это типы коллекций

# t= (5,7,"privet") # картеж
# print(type(t))
# print(len(t))
# s={8,8,8,8,8,8,8}
# s.add(777)
# s.discard(77777)# пытается удалить
# print(s)

d = {"дядя петя": 65465468, "Тетя ира" : [546544,5454]}
d["дядя ваня"] = 46464
d["Тетя ира"].append(46766)
# print(d)
# del d["дядя ваня"]
# print(d)
# print(d.keys())
# print(d.values())
# for k in d:
#     print(k)
for key, value in d.items():
    print(f"{key}---{value}")

