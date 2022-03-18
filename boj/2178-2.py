import sys

N, M = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

queue = [[0, 0]]

while queue:
    row, col = queue.pop(0)
    last = [row, col]
    if row == N-1 and col == M-1:
        break
    for i in range(4):
        new_row = row + dxs[i]
        new_col = col + dys[i]
        if 0 <= new_row < N and 0 <= new_col < M and matrix[new_row][new_col] == 1:
            matrix[new_row][new_col] = matrix[row][col] + 1
            queue.append([new_row, new_col])

print(matrix[N-1][M-1])