# 03. Stack

## Backtracking

* 해를 찾는 도중에 '막히면'(=해가 아니면) 되돌아가서 다시 해를 찾아가는 기법
* 최적화 문제와 결정 문제를 해결할 수 있다
* DFS랑 뭐가 다르냐면 해결책으로 이어질 '것 같지 않으면' 바로 다른 경로로 가버림: 불필요한 경로를 미리 차단해서 모든 후보를 검사하지 않는 거임!! 그러므로 더 효율적이게 된다
* 오 알겠어



### (일단) 부분집합

```python
# i: 부분집합에 포함될지 결정할 원소의 인덱스
# N: 전체 원소 갯수
def f(idx, N):
    if idx == N:  # 밑에서 idx를 올릴 거니까 idx가 N까지 닿으면 부분집합 완,
        print(*bit, end=" ")
        print()
        return
    else:
        bit[idx] = 1  # 이거 넣구
        f(idx + 1, N)  # 그 다음 탐색
        bit[idx] = 0  # 다시 여기에 와서 이거 빼고 탐색
        f(idx + 1, N)  # 그 다음 탐색
    return


a = [1, 2, 3]  # f함수로 나중에 소환시키면 댐 이건 패스하깨
bit = [0] * len(a)
f(0, 3)  # 0과 1로 나오는 넣었다 뺐다
```



### 부분집합의 합

* {1, 2, 3, 4} 인 부분집합은 {1, 2, 3}의 합을 알고 있으면 거기에 4를 더하기만 하면 알 수 있음! 그 원리

```python
# 부분집합 원소 합이 K인 부분집합 구하기

def f2(i, N, K):
    global count
    count += 1
    if i == N:  # 완성되면
        s = 0
        for j in range(N):
            if bit[j]:  # 인덱스 보고 들어가면
                s += a[j]  # 실제 그 숫자 더함
        if s == K:  # 합이 K라면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=" ")  # 도로로록
            print()
    else:
        bit[i] = 1
        f2(i+1, N, K)
        bit[i] = 0
        f2(i+1, N, K)


count = 0
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * len(a)
f2(0, len(a), 15)
print(count)  # 15든 55든 2047로 항상 같음 이거는 백트래킹 없이 끝까지 모든 걸 돌리는 거라
```

* 백트래킹을 해보쟈

```python
def f3(i, N, s, t):
    # i: 부분집합에 포함될지 결정할 원소의 인덱스
    # N: 전체 원소 갯수
    # s: 이전까지 고려된 원소의 합
    # t: 목표값
    global count
    count += 1
    if s == t:  # 목표값에 도달하면
        for j in range(N):
            if bit[j]:
                print(a[j], end=" ")
        print()
    elif i == N:  # 더 이상 고려할 원소가 없으면
        return  # 돌아가보자고
    elif s > t:  # 합이 목표값을 넘어버린 경우
        return
    else:
        bit[i] = 1
        f3(i+1, N, s+a[i], t)  # 1이면 지금 얘를 더한 게 여태까지 고려된 원소의 합이 되는 것
        bit[i] = 0
        f3(i+1, N, s, t)  # 0이니까 지금 얘는 더하지 않고 지나가는 것


count = 0
N = 10
a = [x for x in range(1, N+1)]
bit = [0] * N
t = 15
f3(0, N, 0, t)
print(count)  # 55처럼 끝까지 돌아야 할 때는 2047로 같지만 중간 값(15)이면 백트래킹이 되어서 훨씬 줄어든다
```

```python
# 더더더 백트래킹 해보기


def f3(i, N, s, t, rs):
    # i: 부분집합에 포함될지 결정할 원소의 인덱스
    # N: 전체 원소 갯수
    # s: 이전까지 고려된 원소의 합
    # t: 목표값
    # rs: 여태 넣니 마니 하던 것들의 최대값 그 이상의 원소를 전부 합한 거
    global count
    count += 1
    if s == t:  # 목표값에 도달하면
        for j in range(N):
            if bit[j]:
                print(a[j], end=" ")
        print()
    elif i == N:  # 더 이상 고려할 원소가 없으면
        return  # 돌아가보자고
    elif s > t:  # 합이 목표값을 넘어버린 경우
        return
    elif s + rs < t:  # ★★★ 예를 들어 4개 중에 2개 넣고 더했는데 그 4개 뒤에 남은 것들 다 더한 거랑 2개 더해도 목표치에 못 다다르면
        return
    else:
        bit[i] = 1
        f3(i+1, N, s+a[i], t, rs-a[i])  # 1이면 지금 얘를 더한 게 여태까지 고려된 원소의 합이 되는 것
        bit[i] = 0
        f3(i+1, N, s, t, rs-a[i])  # 0이니까 지금 얘는 더하지 않고 지나가는 것


N = 10
a = [x for x in range(1, N+1)]
bit = [0] * N
t = 55
count = 0
f3(0, N, 0, t, sum(a))
print(count)  # 21 혁 신 적
```



### 순열

```python
# 기본 알고리즘

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i], end=" ")
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)  # 다음 후보군 좀 찾아 봐
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
```

* 1, 2, 3으로 순열을 만들어보자
* 최대한 데이터 하나를 쓰려면 P = [1, 2, 3]에서 1로 시작하는 건 1과 1을 바꾸기(그대로), 2로 시작하는 건 1과 2를 바꾸기([2, 1, 3]), 3으로 시작하는 건 1과 3을 바꾸기([3, 2, 1])
* 두 번째 자리도 같다 2, 3 이고 그 다음 3 넣으려고 2와 3을 바꾸기

```python
# 알고리즘으로 쓰자면
def my_func(i, N):
    if i == N:  # 순열 완성
        pass
    else:
        # P[i] 결정하고
        my_func(i+1, N)  # 다음 거 결정하는 재귀
        # P[i] 다시 돌아오기 (P[i]에 그 다음 거(2였으면 3) 넣으려고)
```

















## 분할 정복 알고리즘