from sys import stdin
from collections import deque

N = int(input())
targets = list(map(int, input().split()))
M = int(input())

edges = [[] for _ in range(N+1)]
for i in range(M):
    a, b = list(map(int, input().split()))
    edges[a].append(b)
    edges[b].append(a)

visited = [0] * (N+1)


def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        now = queue.popleft()
        for j in edges[now]:
            if visited[j] == 0:
                visited[j] = visited[now] + 1
                queue.append(j)


bfs(targets[0])
if visited[targets[1]] != 0:
    print(visited[targets[1]])
else:
    print(-1)
