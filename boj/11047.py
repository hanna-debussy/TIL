from sys import stdin

N, value = list(map(int, input().split()))
array = []
for i in range(N):
    array.append(int(input()))

count = 0
for i in range(1, N+1):
    while value > 0:
        value = value - array[-i]
        count += 1
    if value < 0:
        value += array[-i]
        count -= 1

print(count)
