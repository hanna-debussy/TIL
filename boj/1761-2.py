import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

N = int(input())
edges = {}
for _ in range(N-1):
    a, b, c = map(int, input().split())
    if a not in edges:
        edges[a] = []
        edges[a].append([b, c])
    else:
        edges[a].append([b, c])
    if b not in edges:
        edges[b] = []
        edges[b].append([a, c])
    else:
        edges[b].append([a, c])

q = int(input())
matrix = [list(map(int, input().split())) for _ in range(q)]


for i in range(q):
    visited = []
    deq = deque()
    start, target = matrix[i]
    deq.append([start, 0])
    visited.append(start)
    while deq:
        menow, distance = deq.popleft()
        nodes = edges[menow]
        for node in nodes:
            if node[0] == target:
                distance += node[1]
                print(distance)
                break
            else:
                if node[0] not in visited:
                    visited.append(node[0])
                    deq.append([node[0], distance+node[1]])
