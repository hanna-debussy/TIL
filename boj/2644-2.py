from sys import stdin

N = int(input())
targets = list(map(int, input().split()))
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(M)]

edges = [[] for _ in range(N)]

for i in range(M):
    edges[matrix[i][0]].append(matrix[i][1])

count = 0
visited = []
for i in range(N):
    visited.append(i)

last = []
queue = [[targets[0], 0]]
while queue:
    to_visit = queue.pop(0)
    last = to_visit
    if not edges[to_visit[0]]:
        for j in edges[to_visit[0]]:
            to_visit[1] += 1
            queue.append([j, to_visit[1]])
            to_visit[1] -= 1
    for k in edges:
        if not k:
            continue
        else:
            for m in range(len(k)):
                if k[m][0] == to_visit:
                    to_visit[1] += 1
                    queue.append([k, to_visit[1]])
                    to_visit[1] -= 1


print(last[1])
"""
9
7 8
7
1 2
1 3
2 7
3 8
2 9
4 5
4 6
"""