from sys import stdin
from collections import deque

floors, start, company, up, down = map(int, input().split())

visited = [0] * (floors+1)
visited[start] = 1

deq = deque()
deq.append(start)

found = False

while deq:
    now = deq.popleft()
    if now == company:
        found = True
        print(visited[now]-1)

    cases = [now+up, now-down]
    for case in cases:
        if 0 < case <= floors and visited[case] == 0:
            visited[case] = visited[now]+1
            deq.append(case)

if not found:
    print("use the stairs")
