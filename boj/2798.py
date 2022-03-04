from sys import stdin

N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))

max_num = 0
total = 0

for i in range(0, N-2):
    total += cards[i]
    for j in range(i+1, N-1):
        total += cards[j]
        for k in range(j+1, N):
            total += cards[k]
            if max_num < total <= M:
                max_num = total
            total -= cards[k]
        total -= cards[j]
    total -= cards[i]

print(max_num)
