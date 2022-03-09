from sys import stdin

N = int(input())
array = [i for i in range(N, 0, -1)]

while len(array) > 1:
    temp_list = []
    is_even = False
    if len(array) % 2 == 0:
        is_even = True
    for i in range(1, len(array)//2 + 1):
        temp_list.append(array[-i*2])
    if is_even is True:
        temp_list.reverse()
        array = temp_list
    else:
        temp_list.reverse()
        first = temp_list.pop()
        array = [first] + temp_list

print(*array)
