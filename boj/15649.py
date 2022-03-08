from sys import stdin

N, M = list(map(int, input().split()))
array = [n for n in range(1, N+1)]
count = 0
sub_list = []


def subset(array, M, N):
    global count
    for i in range(len(array)):
        sub_list.append(array[i])
        count += 1
        array.pop(i)
        if count < M:
            subset(array, M, N)
        else:
            print(*sub_list)
        count -= 1
        array.append(sub_list.pop(-1))
        array.sort()


subset(array, M, N)
