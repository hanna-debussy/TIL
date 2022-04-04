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
    key = [float("inf")]*(N+1)		# 가중치 최대값 이상으로 초기화
    pi = [None]*(N+1)
    key[start] = 0					# 시작정점의 가중치를 0으로 설정
    
    for _ in range(N):				# 정점의 개수만큼			
        min_vetex = 0
        min_key = float("inf")
        
        for i in range(N):			# 방문하지 않은 정점들 중 최소 가중치 정점 찾기
            if MST[i] is False and key[i] < min_vertex:
               	min_vertex = i
                min_key = key[i]
        MST[min_vertex] = True		# 방문 처리
        
        for vertex, val in enumerate(graph[min_vertex]):
            if MST[vertex] is False and val < key[veretx]:
                key[vertex] = val				# 가중치 갱신
                pi[vertex] = min_vertex			# 부모 정점 갱신
```



## Kruskal 알고리즘

사이클이 생기지 않도록 n-1개의 간선을 선택하는 방식.kinda 그리디 알고리즘이구나... 간선을 선택해나가는 과정에 여러 개의 트리가 존재한다

1. 모든 간선을 가중치에 따라 오름차순으로 정렬한다
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 만든다
   &rarr; 이때 사이클이 존재하면 패스하고 그 다음으로 가중치가 낮은 간선을 선택
3. n-1개의 간선이 선택될 때까지 반복 수행















