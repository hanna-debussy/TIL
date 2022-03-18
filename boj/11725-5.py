import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
matrix = [[] for _ in range(N+1)]

for _ in range(N-1):
    temp = list(map(int, sys.stdin.readline().split()))
    matrix[temp[0]].append(temp[1])
    matrix[temp[1]].append(temp[0])

parent = [0] * (N+1)
stack = []


def find_child(v):
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