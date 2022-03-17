from sys import stdin

N, M, V = list(map(int, input().split()))

edges = [[0] * (N+1) for _ in range(N+1)]
# count_list = []
for i in range(M):
    temp = list(map(int, input().split()))
    # count_list.extend(temp)
    edges[temp[0]][temp[1]] = 1
    edges[temp[1]][temp[0]] = 1

# count = len(set(count_list))


# DFS
visited = [0] * (N+1)
stack_d = []


def dfs(v):
    visited[v] = 1
    stack_d.append(v)

    for j in range(1, N+1):
        if visited[j] == 0 and edges[v][j] == 1:
            dfs(j)


dfs(V)
print(*stack_d)


# BFS
stack_b = []
visit = [V]
visited_b = [0] * (N+1)

while visit:
    here = visit.pop(0)
    if visited_b[here] == 1:
        continue
    else:
        stack_b.append(here)
        visited_b[here] = 1
        for k in range(1, N+1):
            if visited_b[k] == 0 and edges[here][k] == 1:
                visit.append(k)

print(*stack_b)