from sys import stdin
from collections import deque

N, M = list(map(int, input().split()))

deq = deque()
time = 0
visited = [0] * (10**5 + 1)
deq.append([N, 0])

while deq:
    menow = deq.popleft()
    if menow[0] == M:
        time = menow[1]
        break
    visited[menow[0]] = 1
    case = [menow[0]+1, menow[0]-1, menow[0]*2]
    for i in case:
        if visited[i] == 0:
            deq.append([i, menow[1]+1])

print(time)
