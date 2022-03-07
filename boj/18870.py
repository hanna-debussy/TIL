from sys import stdin

N = int(input())
array = list(map(int, input().split()))

answer = []

for i in range(N):
    check = []
    count = 0
    for j in range(N):
        if array[j] not in check:
            if array[i] > array[j]:
                check.append(array[j])
                count += 1
    answer.append(count)

print(*answer)
