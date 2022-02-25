# 4. Queue

놀이공원 앞에 서있는 줄을 생각하면 된다. 먼저 선 사람이 먼저 들어가는 것처럼 먼저 들어간 값을 먼저 꺼낼 수 있다.

front: 저장된 첫 번째 원소의 인덱스. 한 마디로 마지막으로 삭제된 위치(내 앞사람이 놀이공원 들어가고 내가 줄의 첫 빠따인 셈)
rear: 저장된 마지막 원소의 인덱스. 마지막으로 저장된 위치

**front와 rear는 인덱스에서 왔다갔다 하는 거지 원소 자체를 의미하는 게 아님**

front 자리와 rear 자리가 같다는 건 queue가 비어있다는 의미



## 큐의 종류

### 선형큐

* 가장 처음 만들 때 front = rear = -1로 설정
* 공백 상태: front == rear
* 포화 상태: rear == len(queue) - 1



1. 삽입 enQueue(item)
   : rear 값을 하나 증가시켜서 새로 넣을 자리를 마련하고 그 인덱스에 item을 저장
2. 삭제 deQueue()
   : front 값을 하나 증가시키고 그 자리에 있던 애를 반환함 (not 삭제)
3. 검색 Qpeek()
   : front+1에 있는 원소, 즉 가장 앞에 있는 원소를 검색하여 반환

```python
front = -1
rear = -1
Q = [0]*10

# enQueue
rear += 1
Q[rear] = 1  # 0에 1 집어넣은 거
rear += 1
Q[rear] = 2  # 1에 2

#deQueue
front += 1
print(Q[front])  # 2 아니고 1이 나온다
```



but 선형큐의 단점은...

1. rear가 가장 끝에 있으면 포화 상태로 인식해버린다 근데 front가 아직 거기가 아니라면? 맨 끝이 비는 거임
   * 그래서 연산할 때마다 뒤에 애를 앞으로 보내버려서 보호해야 한대 약간 배열의 앞과 뒤를 붙여서 원형으로 되어있다고 생각...하자는 게 원형큐



### 원형큐

![소스 이미지 보기](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https:%2F%2Fblog.kakaocdn.net%2Fdn%2Fbk7QaM%2FbtqEITHzlyG%2FsPazJhxYBKaIg4MtXXZeak%2Fimg.png)

* 초기 공백을 -1이 아닌 0으로 설정
* 포화 상태를 front가 가리키는 그 곳 *빼고* 전부 다 차있는 상태라고 본다 꽉 찼을 때에도 한 자리가 비어있다는 말 그래서 결론적으로 rear 다음이 front면 다 차있는 거임
* 공백상태는 머 front = rear



### 우선순위 큐

* 선입선출이 아니라 우선순위가 높은 순서대로 먼저 나가게 된다



## 큐는 어디서 쓰이나요

### 버퍼

: 데이터를 전송하는 동안 일시적으로 그 데이터를 보관해놓는 메모리

헐 버퍼링에 버퍼가 이거래 버퍼를 채우는 동작... 데엠
일반적으로 네트워크와 관련된 기능에서 사용



### BFS (Breadth Frist Search)

![소스 이미지 보기](https://th.bing.com/th/id/R.c1086d93cc9a98f9da3d26f6925afa66?rik=5jsjqnoi5SjnXw&riu=http%3a%2f%2fcfile6.uf.tistory.com%2fimage%2f215F5B4F591403240AB56B&ehk=%2bankMxVVb6RrPMCqaoTdpCIkou46Ik7WMIT3iV74heY%3d&risl=&pid=ImgRaw&r=0)

아하

* visited에 1을 넣으면 가야할 곳 리스트에 1이 갈 수 있는 234를 넣겠지 그러면 앞에서부터 차례대로 2가 visited에 들어가면 또 걔의 56이 들어가고 visited에 3 4 차례대로 들어가면 뒤에 78 들어가서 결국 5678이 차례대로 또 쪼로록 들어와있음 뭔말인지 알겠지 또 걔네를 또 조로록 탐색하면 가야할 곳에 또 차례대로 들어가있고 데엠
* `while not 가야할 곳:` 이렇게 짜야겠지





* 출발-도착 최소 이동거리

```python
def BFS(G, v, n):  # 그래프 G, 탐색시작점 v
    visited = [0] * (n+1)  # 정점의 개수 n
    queue = []
    queue.append(v)
    visited[v] = 1  # 1로 체크하네 여기서는
    while queue:
        t= queue.pop(0)
        visit(t)  # 들러서 할 거 하라고
        for i in G[t]:  # t와 연결된 점들에 대해 그니까 다음 층에 대해
            if not visited[i]:  # 거기가 ㅇㅣ미 간 곳이 아니라면
                queue.append(i)  # 가야 할 곳 리스트에 넣어
                visited[i] = visited[n] + 1  # 갔던 곳 체크했으니까 다음 체크할 박스로 궈
```









