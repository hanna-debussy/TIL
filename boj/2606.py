from sys import stdin

N = int(input())
E = int(input())
edges = []
for _ in range(E):
    temp = list(map(int, input().split()))
    edges.append(temp)

max_com = 0
for i in range(E):
    if max_com < edges[i][0]:
        max_com = edges[i][0]
    if max_com < edges[i][1]:
        max_com = edges[i][1]

matrix = [[0]*(max_com+1) for _ in range(max_com+1)]

for j in range(E):
    matrix[edges[j][0]][edges[j][1]] = 1
    matrix[edges[j][1]][edges[j][0]] = 1


stack = []
visited = [0] * (max_com+1)


def dfs(v):
    stack.append(v)

    now = stack.pop()
    if visited[now] == 0:
        visited[now] = 1
        for k in range(max_com+1):
            if visited[k] == 0 and matrix[now][k] == 1:
                dfs(k)


dfs(1)

answer = -1
for n in visited:
    if n == 1:
        answer += 1

print(answer)