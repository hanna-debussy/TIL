from sys import stdin

N = int(input())
edges = []
for _ in range(N-1):
    temp = list(map(int, input().split()))
    edges.append(temp)

matrix = [[] for _ in range(N+1)]

for edge in edges:
    matrix[edge[0]].append(edge[1])
    matrix[edge[1]].append(edge[0])

parent = [0] * (N+1)
stack = []


def find_child(v):
    # stack.append(v)
    # now = stack.pop()

    for i in matrix[v]:
        if parent[i] == 0:
            parent[i] = v
            find_child(i)


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