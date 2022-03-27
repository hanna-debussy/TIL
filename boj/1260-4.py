import sys

N, M, V = map(int, input().split())

edges = [[] for _ in range(N+1)]
for m in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

for edge in edges:
    edge.sort(reverse=True)

visited = [0] * (N+1)
stack = [V]
dfs = []

while stack:
    to_visit = stack.pop()
    if visited[to_visit] == 0:
        dfs.append(to_visit)
        visited[to_visit] = 1
        followings = edges[to_visit]
        for following in followings:
            if visited[following] == 0:
                stack.append(following)

print(*dfs)

queue = [V]
bfs = []
b_visited = [0]*(N+1)

while queue:
    menow = queue.pop(0)
    if b_visited[menow] == 0:
        bfs.append(menow)
        b_visited[menow] = 1
        edges[menow].sort()
        queue.extend(edges[menow])

print(*bfs)
