from sys import stdin

N = int(input())
all_edges = []
edges = []
for _ in range(N-1):
    temp = list(map(int, input().split()))
    all_edges.extend(temp)
    edges.append(temp)

matrix = [[0]*(N+1) for _ in range(N+1)]

for edge in edges:
    matrix[edge[0]][edge[1]] = 1
    matrix[edge[1]][edge[0]] = 1

check = [0] * (N+1)
for alls in all_edges:
    check[alls] += 1

parent = [0] * (N+1)
queue = [1]
count = [0] * (N+1)

while queue:
    now = queue.pop(0)
    count[now] += 1
    for i in range(N+1):
        if matrix[now][i] == 1 and parent[i] == 0:
            queue.append(i)
            count[i] += 1
            parent[i] = now

for n in range(2, N+1):
    print(parent[n])


"""
7
1 6
6 3
3 5
4 1
2 4
4 7
"""