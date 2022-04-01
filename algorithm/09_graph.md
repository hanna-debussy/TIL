# 9. Graph

## 그래프

### 그래프,,,?

* 아이템들과 그들 사이의 연결 관계
* 정점vertex들의 집합과 이들을 연결하는 간선edge들의 집합으로 구성
  * |V|: 정점의 개수
  * |E|: 간선의 개수
  * |V|개의 정점을 가지는 그래프는 최대 |V|(|V|-1)/2 개의 간선이 가능(1~(|V|-1)개 합
* 선형이나 트리로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현할 수 있다



### 그래프 유형

* 무향 그래프: 양방향... 방향이 없다고
* 유향 그래프: 방향 있을 유
* 가중치 그래프: 간선에 숫자(가중치)가 있음
* 사이클 없는 방향 그래프 DAG: 약간 트리 느낌
* 완전 그래프: 그냥 모두가 다 이어져있음



### 그래프 경로

* 간선들을 순서대로 나열한 거
* 단순 경로: 경로 중 한 정점을 최대한 한 번만 지나는 닌자경로



### 그래프 표현

인접 행렬, 인접 리스트 방법이 있는데 으음~ 무슨 말인지 알겠어



## 그래프 순회(탐색)

### DFS

1. 스택 사용하기

   ```python
   # Template
   
   stack = []
   visited = [False]*(vertex+1)
   
   def dfs(vertex):
       stack.append(vertex)
       visited[vertex] = True
       
       while stack:
           menow = stack.pop()
           # 방문해서 할 거 처리하고
           
           for adjacent in edges[menow]:
               if visited[adjacent] is False:
                   stack.append(adjacent)
                   visited[menow] = True
   ```

   

2. 재귀 사용하기

   ```python
   # Template
   
   def recursion(graph, vertex):
       visited[vertex] = True
       
       for adjacent in edges[vertex]:
           if visited[adjacent] is False:
               recursion(graph, adjacent)
               
       # 만약 중복 경로를 허용한다면
       visited[vertex] = False
   ```



### BFS

큐!!!!!!!!!!!!!!!!!!!!!

```python
# Template

def bfs(graph, vertex):
    queue = []
    queue.append(vertes)
    visited[vertex] = True
    
    while queue:
        front = queue.pop(0)
        for adjacent in edges[front]:
            if visited[adjacent] = False:
                queue.append(adjacent)
                visited[adjacent] = True
```