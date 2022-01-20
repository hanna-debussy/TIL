a, b, *c = 5, 6, 7, 8, 9
print(a)  # 5
print(b)  # 6
print(c)  # 


lst = [1, 2, 3, 4]
i, j, *k = lst
print(i, j, k)  #
print(i, j, *k)



dict_a = {1: 1, "two": 2, 3: "three", 1: 4}  # 제일 마지막이 살아남는다
print(dict_a)  # {1: 4, 2: 2, 3: 3}

print(type(dict_a.keys()))  # 
print(dict_a.values())
print(type(dict_a.items()))


print(True and False and True and True and False)
# and는 false가 나오는 순간 value가 정해진다

True or False or True or True or False
# or는 true가 나오는 순간 value가 정해진다







# python hap.py