import sys

N, M = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

queue = [[0, 0, 1]]
last = []

while queue:
    row, col, count = queue.pop(0)
    last = [row, col, count]
    if row == N-1 and col == M-1:
        break
    for i in range(4):
        new_row = row + dxs[i]
        new_col = col + dys[i]
        if 0 <= new_row < N and 0 <= new_col < M and matrix[new_row][new_col] == 1:
            matrix[row][col] = 0
            queue.append([new_row, new_col, count+1])

print(last[2])
