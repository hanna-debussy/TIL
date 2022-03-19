from sys import stdin

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def bfs(r, c):
    global width
    width += 1
    matrix[r][c] = 0
    for i in range(4):
        new_r = r + dxs[i]
        new_c = c + dys[i]
        if 0 <= new_r < N and 0 <= new_c < N and matrix[new_r][new_c] == 1:
            bfs(new_r, new_c)


count = 0
widths = []
for row in range(N):
    for col in range(N):
        width = 0
        if matrix[row][col] == 1:
            bfs(row, col)
            widths.append(width)
            count += 1

print(count)
widths.sort()
for k in range(len(widths)):
    print(widths[k])


"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""