# 01 뭐부터 공부해야 하지?

배우긴 하는데 어디서부터 무엇이 알고리즘인지 모르겠다



## 50

101 이전에 50이 있다고들 해서 50이라고 해봤다

* list를 답처럼 띄어쓰기로 출력하는 방법

  ```python
  for tc in range(1, T+1):
      print(f"#{tc}", end=" ")
      print(*matrix)
  ```

  

* 주어진 N*N 배열을 list 형태로 만드는 법

* ```python
      matrix = [list(map(int, input().split())) for _ in range(N)]
  ```

* 2차원 배열 꺼내서 출력하는 법

  ```python
  for tc in range(1, T+1):
      N = int(input())
      answer = spiral(N)
      print(f"#{tc}")
      for n in answer:
          print(*n)
  ```
  
  

* 

* 

* 0 두르는 법

  ```python
  matrix = [[0] * (N+2)]
  for _ in range(N):
      row = [0, *list(map(int, input().split())), 0]
      matrix.append(row)
  matrix.append([0]*(N+2))
  ```

  

  