# 03. Stack

쌓여있는 ~~할것~~ 자료 구조를 가진 저장소

* 스택 자료는 선형 구조를 갖는다
* 마지막에 삽입한 자료가 가장 먼저 꺼내진다 - 후입 선출

stack overflow의 stack이 이 stack이다. 그 로고를 생각하면 딱 될 듯. 아니면 실탄 넣는 거랑 같겠다. 



근데? 차곡차곡 쌓는 1차원 배열을 사용하면 스택 크기 변경이 어렵다
(&rarr; 저장소를 동적으로 할당하여 스택을 구현하자!: 동적 연결리스트)



## 재귀호출

스택으로 만들 수 있따

### ex) A를 B로 복사하는 방법

```python
def f(i, N):
    if i == N:
        return B
	else:
        B[i] = A[i]
        f(i+1, N)
        

A = [10, 20, 30]
B = [0] * 3
f(0, 3)
print(B)
```



근데? 재귀함수로 구현하면 엄청난 중복 호출이 생긴다는 문제가 생긴다



## Memoization

중복 호출하지 말고 한 번 구했으면 어디다 저장해두자는 말임

### 피보나치(feat. memoization)

```python
# memo에 저장을 해두자
# fibo1(n)을 memo[n]에 넣어두는 것

def fibo1(n):
    if n >= 2 and memo[n] == 0:  # 아직 한 번도 돈 적이 없을 때도 포함
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]


n = 7

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n))
print(memo)
```



## DP(Dynamic Programming)

* 동적계획 알고리즘: 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결
* 재귀처럼 함수를 자꾸 호출하는 게 아니고 그냥 for문을 돌리는 거라 더 부담이 없다?

### 피보나치 feat. DP

```python
n = 7

fibo = [0] * (n+1)
fibo[0] = 0
fibo[1] = 1

for i in range(2, n+1):  # 2부터 차곡차곡
    fibo[i] = fibo[i-1] + fibo[i-2]  # append로 해도 됨 [0, 1] 해놓고
print(fibo)
```



## DFS(깊이우선탐색)

* 시작 정점에서 한 방향으로 쭉 깊이 가다가 더 이상 갈 곳이 없게 되면 가장 마지막에 만났던 정점으로 되돌아가서 다른 방향으로 가서 다시 탐색
* 그림이... 그림은 DFS 검색하면 정말 많은 사람들이 그래프를 움짤로 만들어놨으니 검색해볼 것
* cf) BFS: 최단길이 검색할 때
