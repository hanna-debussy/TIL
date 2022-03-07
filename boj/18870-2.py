from sys import stdin

N = int(input())
array = list(map(int, input().split()))

sorted_array = sorted(list(set(array)))
answer = []

for i in array:
    for j in range(len(sorted_array)):
        if i == sorted_array[j]:
            answer.append(j)

print(*answer)
