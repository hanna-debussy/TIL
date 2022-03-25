from sys import stdin
from collections import deque

N, M = list(map(int, input().split()))

deq = deque()
time = 0
visited = [0] * (10**5 + 1)
deq.append(N)

while deq:
    menow = deq.popleft()
    if menow == M:
        time = visited[menow]
        break

    case = [menow+1, menow-1, menow*2]
    for i in case:
        if 0 <= i < len(visited) and visited[i] == 0:
            visited[i] = visited[menow] + 1
            deq.append(i)

print(time)
