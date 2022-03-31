import sys
sys.setrecursionlimit(10**6)

str_list = list(input())


def recursion(array):
    new_array = []

    for i in range(len(array)):
        if array[i] == "(" or array[i] == "[":
            new_array.append(array[i])

        elif array[i] == ")":
            cnt1 = 0
            for j in range(len(new_array)-1, -1, -1):
                cnt1 += 1
                if new_array[j] == "[":
                    print(0)
                    break
                elif new_array[j] == "(":
                    if cnt1 == 1:
                        new_array.pop()
                        new_array.append(2)
                        break
                    elif cnt1 == 2:
                        double = new_array.pop(j+1)
                        double = double*2
                        new_array.pop(j)
                        new_array.append(double)
                        break
                    else:
                        new_array.append(")")
                        break

        elif array[i] == "]":
            cnt2 = 0
            for j in range(len(new_array)-1, -1, -1):
                cnt2 += 1
                if new_array[j] == "(":
                    print(0)
                    break
                elif new_array[j] == "[":
                    if cnt2 == 1:
                        new_array.pop()
                        new_array.append(3)
                        break
                    elif cnt2 == 2:
                        triple = new_array.pop(j+1)
                        triple = triple*3
                        new_array.pop(j)
                        new_array.append(triple)
                        break
                    else:
                        new_array.append("]")
                        break

        else:
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




