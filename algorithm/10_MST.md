# 최소 신장 트리 MST

* 신장 트리
  : n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

* 최소 신장 트리
  : 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리



## Prim 알고리즘

하나의 정점에서 그 간선들 중에 하나씩 선택하면서 MST를 만들어가는 방식

1. 임의의 정점을 하나 선택
2. 선택한 정점의 이어진 정점들 중 최소 가중치인 정점 선택
3. 모든 정점이 선택될 때까지 1, 2를 반복

```python
# pi: 간선 정보들이 저장
# key: pi에 저장된 간선들의 가중치를 저장

def prim(graph, start):
    MST = [False]*(N+1)				# MST 포함 여부(일종의 visited)
    mins = [float("inf")]*(N+1)		# 가중치 최대값 이상으로 초기화
    pi = [None]*(N+1)
    mins[start] = 0					# 시작정점의 가중치를 0으로 설정
    
    for _ in range(N):				# 정점의 개수만큼			
        min_vetex = 0
        min_key = float("inf")
        
        for i in range(N):			# 방문하지 않은 정점들 중 최소 가중치 정점 찾기
            if MST[i] is False and mins[i] < min_vertex:
               	min_vertex = i
                min_key = mins[i]
        MST[min_vertex] = True		# 방문 처리
        
        for vertex, val in enumerate(graph[min_vertex]):
            if MST[vertex] is False and val < mins[veretx]:
                mins[vertex] = val				# 가중치 갱신
                pi[vertex] = min_vertex			# 부모 정점 갱신
```



## Kruskal 알고리즘

사이클이 생기지 않도록 n-1개의 간선을 선택하는 방식. kinda 그리디 알고리즘이구나... 간선을 선택해나가는 과정에 여러 개의 트리가 존재한다

1. 모든 간선을 가중치에 따라 오름차순으로 정렬한다
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 만든다
   &rarr; 이때 사이클이 존재하면 패스하고 그 다음으로 가중치가 낮은 간선을 선택
3. n-1개의 간선이 선택될 때까지 반복 수행

find와 union이라는 함수를 만들어서 사용하기 때문에 find-union 알고리즘, 서로소집합 알고리즘이라고도 한대



```python
import sys


# 경로의 대장(부모)이 누구냐
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


# 지금 경로의 대장(부모) 찾기 (일종의 간선을 연결)
def union(parent, a, b):
    parent[find(b)] = find(a)


def kruskal():
    total = 0
    for w, u, v in edges:
        # u와 v가 서로 다른 집합에 속해있을 때 (같으면 사이클이 생겨서 트리 성립 불가)
        if find_set(u) != find_set(v):
            union(parent, u, v)
            total += w
    
    return total


# V: 정점 개수, E: 간선 개수
V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

# 비용순으로 정렬을 해야 그리디가 가능
edges.sort()

parent = [i for i in range(V+1)]
result = kruskal()
print(result)
```



## Dijkstra 알고리즘

가중치가 있는 트리에서 임의의 두 점을 잇는 최소 거리/비용... 등을 계산할 때 쓰인다. 위의 두 알고리즘과 다른 점은 저 둘은 거시적으로 봤을 때 '모든' 점을 잇는 최소 거리/비용을 구하는 것이기 때문에 그 트리에서 임의의 두 점을 뽑았을 때 그 둘 사이가 최소 거리/비용인 건 아니다!!



```python
import sys
import heapq

sys.stdin = open("input.txt")

T = int(input())


# heapq 없이 구현
def dijkstra(start):
    global distances, visited
	
    # 시작점 갱신
    distances[start] = 0
    visited[start] = True

    # 일단 시작점으로부터 모든 인접점 이동거리 갱신
    for ee, ww in graph[start]:
        distances[ee] = ww

    # 시작점을 제외하고 (N+1)-1개의 노드에 대해 고려
    for _ in range(N):
        now = 0
        min_val = float("inf")
        for i in range(1, N+1):
            # 방문하지 않았고 시작점과 최단 거리인 노드를 now에 저장
            if not visited[i] and distances[i] < min_val:
                min_val = distances[i]
                now = i
		
        # now에 방문 처리
        visited[now] = True
        # 그 now의 인접 노드들에 대해
        for next_node, next_distance in graph[now]:
            # now를 거쳐 인접 노드를 가는 방법 distance와
            distance = distances[now] + next_distance
            # 지금까지 다른 방법으로 거기 닿는 방법 중 최소거리가 저장되어있던 것을 비교
            if distance < distances[next_node]:
                distances[next_node] = distance

    return


# heapq 사용
def hq_dijkstra(start):
    hq = []
    h_distances[start] = 0
    heapq.heappush(hq, (h_distances[start], start))         # 처음부터 탐색

    while hq:
        # 탐색할 노드 now와 그 거리를 가져와서
        now_distance, now = heapq.heappop(hq)
        # 기존 거리보다 길면 고려할 필요 x
        if h_distances[now] < now_distance:
            continue

        for next_node, next_distance in graph[now]:
            distance = now_distance + next_distance
            if distance < h_distances[next_node]:
                h_distances[next_node] = distance
                heapq.heappush(hq, (distance, next_node))

    return h_distances


for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    visited = [False] * (N+1)
    distances = [float("inf")] * (N+1)

    h_visited = [False] * (N+1)
    h_distances = [float("inf")] * (N+1)

    dijkstra(0)                             # 0번부터
    hq_dijkstra(0)

    print(distances)
    print(h_distances)

    print(f"#{tc} {distances[x]}")          # 임의의 x번까지 (알아서 넣어)
```













