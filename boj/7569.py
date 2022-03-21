from sys import stdin
from collections import deque

M, N, H = list(map(int, input().split()))

matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(matrix)

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
heights = [-1, 1]

queue = deque()
last = 1


