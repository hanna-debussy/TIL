from sys import stdin

N = int(input())
array = list(map(int, input().split()))

sub_list = []
last = 0
if len(array) == 1:
    print(1)
else:
    for i in range(N-1):
        if array[i] < array[i+1]:
            sub_list.append(array[i])
            sub_list.append(array[i+1])

    temp = [sub_list[0]]
    for i in range(N-1):
        if sub_list[i] < sub_list[i+1]:
            temp.append(sub_list[i+1])

    answer = len(temp)
    print(*temp)
    print(answer)
