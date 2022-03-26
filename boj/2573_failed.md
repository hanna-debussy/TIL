# 2573 빙산

아니 실패했는데 도대체 어디서 NameError가 뜨는지 모르겠다 선언되지 않은 변수가 나온다고...?
여튼 첫 실패인데 배운 게 있어서 잠시 메모한다

```python
from sys import stdin
from collections import deque
# 이게 묘하다...
sys.setrecursionlimit(10**5)

R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
year = -1
while True:
    visited = [[0]*C for _ in range(R)]
    deq = deque()
    count = 0
    year += 1
    # 빙산 개수 새기
    for r in range(R):
        for c in range(C):
            if matrix[r][c] != 0 and visited[r][c] == 0:
                deq.append([r, c])
                while deq:
                    row, col = deq.popleft()
                    visited[row][col] = 1
                    for i in range(4):
                        new_row = row + dxs[i]
                        new_col = col + dys[i]
                        if 0 <= new_row < R and 0 <= new_col < C:
                            if matrix[new_row][new_col] != 0 and visited[new_row][new_col] == 0:
                                deq.append([new_row, new_col])
                count += 1
    # 빙산이 두 개 이상이거나 다 녹았을 때 처리
    if count > 1:
        print(year)
        break
    elif count == 0:
        print(0)
        break

    # 빙산 녹이는 for문
    for rr in range(R):
        for cc in range(C):
            if matrix[rr][cc] != 0:
                sea = 0
                for delta in range(3):
                    new_r = rr + dxs[delta]
                    new_c = cc + dys[delta]
                    if 0 <= new_r < R and 0 <= new_c < C and matrix[new_r][new_c] == 0:
                        sea += 1
                matrix[rr][cc] -= sea
            if matrix[rr][cc] < 0:
                matrix[rr][cc] = 0

```

처음 세 번의 시도에서 자꾸 시간초과가 떴다. 분명 논리에는 틀린 게 없어보여서 잠시 구글링을 했더니 python 코드인데 모든 사람이 맨 앞에 *(pypy3으로 제출했다)* 가 적혀있었다.



## pypy3?

일단 대충 pypy3이 비슷한 건가 하면서 보는데 제일 의문이었던 건 `sys.setrecursionlimit(10**5)`이 python에서 돌리면 RecursionError가 난다는 것이었다... 이거 파이썬 언어 맞지 않나?

그거에 대한 대답을 https://imksh.com/46에서 찾았는데 좀 황당하다

*pypy3에서는 정확한 크기를 할당하는 것이 아니라 **대략적으로 크기를 할당**하기 때문에 위와 같은 문제가 발생하게 됩니다.*

신기 그 잡채...

하여간 종합적으로 말하자면 뭐냐면
https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4 에 의하면 pypy3는 자주 쓰이는 코드를 캐싱하는 기능이 있어서 실행속도를 줄일 수 있다고 한다. 대신 그 자주 쓰이는 코드를 저장해두는 메모리가 따로 또 필요하고.

그래서 간단한 코드는 python이 메모리나 속도 면에서 앞서는 거고 반복이 많은 코드는 pypy3가 뛰어나다고 볼 수 있다고 한다.



항상 갸웃거리다가도 무심코 지나쳤는데 이제 궁금증을 풀게 되어서 좋다. 물론 문제 못 푼 건 화난다 ㅎ