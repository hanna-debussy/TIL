from sys import stdin

N = int(input())
edges = []
for _ in range(N-1):
    temp = list(map(int, input().split()))
    edges.append(temp)

matrix = [[0]*(N+1) for _ in range(N+1)]

for edge in edges:
    matrix[edge[0]][edge[1]] = 1
    matrix[edge[1]][edge[0]] = 1

parent = [0] * (N+1)


def find_child(v):
    stack = []
    for i in range(N+1):
        if matrix[v][i] == 1:
            stack.append(i)
    for s in stack:
        if s != 1 and parent[s] == 0:
            parent[s] = v
            find_child(s)


find_child(1)
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