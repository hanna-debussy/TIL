from sys import stdin
from collections import deque

M, N, H = list(map(int, input().split()))

matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(matrix)

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
heights = [-1, 1]

queue = deque()
last = 0


def bfs(height, row, col, day):
    global last

    queue.append([height, row, col, day])
    last = day
    tomato = queue.popleft()
    h = tomato[0]
    r = tomato[1]
    c = tomato[2]
    d = tomato[3]

    while queue:
        for i in range(4):
            new_r = r + dxs[i]
            new_c = c + dys[i]
            if 0 <= new_r < N and 0 <= new_c < M:
                if matrix[h][new_r][new_c] != 1:
                    matrix[h][new_r][new_c] += 1
                if matrix[h][new_r][new_c] == 1:
                    queue.append([height, new_r, new_c, d+1])

        for j in range(2):
            new_h = h + heights[j]
            if 0 <= new_h < H:
                if matrix[new_h][r][c] != 1:
                    matrix[new_h][r][c] += 1
                if matrix[new_h][r][c] == 1:
                    queue.append([new_h, r, c, d+1])


check = 0
bfs(1, 1, 2, 1)
# for z in range(H):
#     for x in range(N):
#         for y in range(M):
#             if matrix[z][x][y] == 1:
#                 check += 1
#                 if check == H*N*M:
#                     print(0)
#                     break
#                 else:
#                     bfs(z, x, y, 1)
#                 cant = 0
#                 for g in range(H):
#                     for e in range(N):
#                         for f in range(M):
#                             if matrix[g][e][f] == 0:
#                                 cant += 1
#
#                 if cant != 0:
#                     print(-1)
#                     break
#                 else:
#                     print(last)
#                     break

print(matrix)
print(last)