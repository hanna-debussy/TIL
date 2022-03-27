import sys
sys.setrecursionlimit(10 ** 6)

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


def tree(n, d):
    global stop
    nodes = edges[n]
    visited.append(n)
    for node in nodes:
        if node[0] == target:
            d = d+node[1]
            print(d)
            stop = True
            # return d
        else:
            if node[0] not in visited:
                if not stop:
                    tree(node[0], d+node[1])


for i in range(q):
    visited = []
    stop = False
    start, target = matrix[i]
    tree(start, 0)
    # answer = tree(start, 0)
    # print(answer)
