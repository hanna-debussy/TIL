# List



## 2*2 배열

* list in list 형태

* input 받는 법

  ```python
  # 2차원 배열에 띄어쓰기가 있을 때
  3
  1 2 3
  4 5 6
  7 8 9
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  
  # 띄어쓰기가 없을 때
  3
  123
  456
  789
  N = int(input())
  arr = [list(map(int, input())) for _ in range(N)]
  
  # 0 사방에 두르기
  arr = [[0]*(N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)] * [[0]*(N+2)]
  # 하나를 알면 둘을 아는 사람이 되자
  ```



### 배열순회

```python
# n*m 배열의 i행 j열


# 행 우선 순회
for i in range(n):
    for j in range(m):
        matrix[i][j]        
        
# 열 우선 순회
for j in range(m):
    for i in range(n):
        matrix[i][j]
        
# 지그재그 순회(행 훑는 게 좌-우 우-좌 좌-우 ...)
for i in range(n):
    for j in range(m):
        # 홀수 행은 우-좌, 거꾸로 와야 한다
        # (i%2)는 0 또는 1이라 (m-1-2*j)를 껐켰
        # 원래는 (m-1-j)-j: 증가하는 j를 감소시키기 위함
        # 앞에 짝수행을 위한 j가 있어서 한 번 더 빼주는 거
        matrix[i][j + (m-1-2*j) * (i%2)]
```



### 델타를 이용한 2차 배열 탐색

: 한 좌표에서 상하좌우 배열 요소 탐색하기 

```python
# 난 CSS 너무 오래 해서 상우하좌가 넘 익숙해져버림
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 보편적
for i in range(4):  # 사방
    new_x = n + dx[i]
    new_y = m + dy[i]
    # 테두리 부분에서 오류가 나지 않게
    if =<=new_x<N and 0<=new_y<M:
        matrix[new_x][new_y]
        
# 간지
for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
# 이하 동일
```



### 전치행렬

행의 좌표와 열의 좌표를 바꾸는 거 

```python
for i in range(N):
    for j in range(N):
        if i < j:  # 모든 i, j에 대해 하면 두 번 뒤집혀서 제자리가 되니까 + 가운데는 제외
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
```



### 부분집합 합

