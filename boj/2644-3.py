from sys import stdin
from collections import deque
# https://jinho-study.tistory.com/885


def bfs(node):
    queue = deque()
    # append: queue의 오른쪽에 넣기
    queue.append(node)
    while queue:
        # popleft: queue의 왼쪽, 그러니까 pop(0)과 같다
        node = queue.popleft()
        # edges에 대해서
        for n in graph[node]:
            # 들르지 않았다면
            if check[n] == 0:
                # 갔다고 체크해주고
                check[n] = check[node] + 1
                # 갖다 넣고
                queue.append(n)


n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
# 아하 그래프를 양방향으로 적어주면 된다
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0] * (n + 1)
bfs(s)
# 오 프린트 안에도 if를 넣을 수 있구나
print(check[e] if check[e] > 0 else -1)


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