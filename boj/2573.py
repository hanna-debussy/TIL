from sys import stdin
from collections import deque
# sys.setrecursionlimit(10**5)

R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
year = -1
while True:
    visited = [[0]*C for _ in range(R)]
    deq = deque()
    count = 0
    year += 1
    for r in range(R):
        for c in range(C):
            if matrix[r][c] != 0 and visited[r][c] == 0:
                deq.append([r, c])
                while deq:
                    row, col = deq.popleft()
                    visited[row][col] = 1
                    for i in range(4):
                        new_row = row + dxs[i]
                        new_col = col + dys[i]
                        if 0 <= new_row < R and 0 <= new_col < C:
                            if matrix[new_row][new_col] != 0 and visited[new_row][new_col] == 0:
                                deq.append([new_row, new_col])
                count += 1
    if count > 1:
        print(year)
        break
    elif count == 0:
        print(0)
        break

    for rr in range(R):
        for cc in range(C):
            if matrix[rr][cc] != 0:
                sea = 0
                for delta in range(3):
                    new_r = rr + dxs[delta]
                    new_c = cc + dys[delta]
                    if 0 <= new_r < R and 0 <= new_c < C and matrix[new_r][new_c] == 0:
                        sea += 1
                matrix[rr][cc] -= sea
            if matrix[rr][cc] < 0:
                matrix[rr][cc] = 0


