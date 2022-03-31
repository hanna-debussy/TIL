import sys
sys.setrecursionlimit(10**6)

str_list = list(input())

new_array = []
result = 0

for i in str_list:

    if i == "(":
        new_array.append(i)
    elif i == "[":
        new_array.append(i)
    elif i == ")":
        if not new_array:
            print(0)
            exit(0)
        temp = 0
        while new_array:
            last = new_array.pop()
            if last == "(":
                if temp == 0:
                    new_array.append(2)
                    break
                else:
                    new_array.append(temp*2)
                    break
            elif last == "[":
                print(0)
                exit(0)
            else:
                temp += int(last)

    elif i == "]":
        if not new_array:
            print(0)
            exit(0)
        temp = 0
        while new_array:
            last = new_array.pop()
            if last == "[":
                if temp == 0:
                    new_array.append(3)
                    break
                else:
                    new_array.append(temp*3)
                    break
            elif last == "(":
                print(0)
                exit(0)
            else:
                temp += int(last)
    else:
        new_array.append(i)

for i in new_array:
    if i == "(" or i == "[" or i == ")" or i == "]":
        print(0)
        exit(0)

result = sum(new_array)
print(result)

