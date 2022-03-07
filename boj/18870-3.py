from sys import stdin

N = int(input())
array = list(map(int, input().split()))

sorted_array = sorted(list(set(array)))
answer = []

for i in array:
    start = 0
    end = len(sorted_array) - 1
    for j in range(N):
        middle = (start + end) // 2
        if i == sorted_array[middle]:
            answer.append(middle)
            break
        elif i > sorted_array[middle]:
            start = middle + 1
        else:
            end = middle

print(*answer)
