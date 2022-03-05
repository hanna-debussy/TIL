from sys import stdin

N = int(input())
matrix = [(list(map(int, input().split())), a) for a in range(N)]

div = 1
rank_list = [0] * N

for i in range(N):
    rank = 1
    for j in range(N):
        if matrix[i][0][0] < matrix[j][0][0] and matrix[i][0][1] < matrix[j][0][1]:
            rank += 1
    rank_list[i] = rank

print(*rank_list)
