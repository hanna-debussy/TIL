from sys import stdin

N = int(input())
array = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

sorted_array = sorted(array)


result = []
for i in range(M):
    find = finds[i]
    start = 0
    end = N - 1
    if find > sorted_array[-1]:
        result.append(0)
    elif find < sorted_array[0]:
        result.append(0)
    while start <= end:
        middle = (start + end) // 2
        if middle+1 < N and sorted_array[middle] <= find <= sorted_array[middle+1]:
            if sorted_array[middle] == find:
                result.append(1)
                break
            elif sorted_array[middle+1] == find:
                result.append(1)
                break
            else:
                result.append(0)
                break
        elif find < sorted_array[middle]:
            end = middle - 1
        elif sorted_array[middle] < find:
            start = middle + 1

print(*result)