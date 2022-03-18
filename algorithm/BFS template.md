**BFS template**

```python
def bfs:
    # queue, visited 등 여기서 초기화
    # queue에 다시 들어온 데이터들 넣고 visited 세팅
    
    while queue:
        # 일단 여기에 종료 조건 처리
        
        for # 돌려야 할 범위에 대해:
            if # 조건에 맞다면:
            	# queue에 삽입
                # 방문 처리
        
```

한 단계씩 탐색하면서 특정 위치나 조건까지의 거리, 단계 수를 셀 때, 미로 이런 거에 BFS를 자주 쓴다



**DFS template**

```python
def dfs(n, 고려할 것):
    if # 종료조건:
    	return
    
    dfs(n+1, 고려할 것 + 지금 했을 때)
    dfs(n+1, 고려할 것 + 지금 안했을 때)
```

