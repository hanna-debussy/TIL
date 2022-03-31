import sys
sys.setrecursionlimit(10**6)

str_list = list(input())


def recursion(array):
    new_array = []

    for i in range(len(array)):

        if array[i] == "(" or array[i] == "[":
            new_array.append(array[i])

        elif array[i] == ")":
            stack = []
            for j in range(len(new_array)-1, -1, -1):
                if new_array[j] == "[":
                    print(0)
                    break
                elif new_array[j] != "(":
                    stack.append(new_array.pop(j))
                elif new_array[j] == "(":
                    if not stack:
                        double = 2
                    else:
                        double = sum(stack)*2
                    new_array.pop(j)
                    new_array.append(double)
                    stack = []
                    break

        elif array[i] == "]":
            stack2 = []
            for j in range(len(new_array)-1, -1, -1):
                if new_array[j] == "(":
                    print(0)
                    break
                elif new_array[j] != "[":
                    stack2.append(new_array.pop(j))
                elif new_array[j] == "[":
                    if not stack2:
                        triple = 3
                    else:
                        triple = sum(stack2)*3
                    new_array.pop(j)
                    new_array.append(triple)
                    break

        else:
            if "(" not in array:
                if "[" not in array:
                    array = [sum(array)]
                    break
            if len(new_array) == 0:
                new_array.append(int(array[i]))
            if new_array[-1] == "[" or new_array[-1] == "]" or new_array[-1] == "(" or new_array[-1] == ")":
                new_array.append(int(array[i]))
            else:
                num = new_array[-1] + int(array[i])
                new_array.pop()
                new_array.append(num)

    if len(array) == 1:
        print(array[0])
    else:
        recursion(new_array)


recursion(str_list)




