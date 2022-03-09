from sys import stdin

N, value = list(map(int, input().split()))
array = []
for i in range(N):
    array.append(int(input()))

count = 0

for i in range(1, N+1):
    temp = value // array[-i]
    value = value - temp*array[-i]
    count += temp
    if value == 0:
        break

print(count)
