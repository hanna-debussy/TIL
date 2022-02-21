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

#### 비트 연산자

* `&` : 비트 단위로 AND 연산
* `|` : 비트 단위로 OR 연산
* `<<` : 피연산자의 비트 열을 왼쪽으로 이동
  * 머랄까 2**n을 뜻함 n개의 모든 부분집합의 수...
* `>>` : 피연산자의 비트열을 오른쪽으로 이동

그래서 `i & (1 << j)`는 i의 j 번째 비트가 1인지 아닌지를 검사할 수 있음!! 맞네



#### 보다 간결하게 부분집합 만들기

```python
matrix = [3, 6, 7, 2, 5, 4]
n = len(matrix)
for i in range(1<<n):  # 연산자를 여기서 걸면 (참고로 1<<n 은 2**n이랑 같다)
    # 여기서부터 0과 1을 통해 저 요소들이 들어가니마니를 결정해서 subset을 만듦
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(matrix[j])
	print(subset)
# 뭔 말이냐면 부분집합 만들 때 넣니마니 하는 걸 0과 1로 하자 이거임
```



### 이진검색

자료가 정렬된 상태여야 한다

검색 과정

* 자료의 중앙에 있는 원소 골라서 중앙 원소와 찾고자 하는 값을 비교
* 목표값이 중앙 원소보다 작으면 왼쪽으로 찾고, 반대는 오른쪽으로 찾음

```python
def binarsySearch(aList, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        if aList[middle] == key:  # 검색 성공
            return True
        elif aList[middle] > key:  # 왼쪽으로
            end = middle - 1
        else:
            start = middle + 1
    return false  # 검색 실패
```

