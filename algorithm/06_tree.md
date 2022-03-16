# 5. Tree이론

## 트리가 뭔데?

* 비선형 구조, 즉 1:n 관계를 가지는 자료 구조를 말한다.(아 그래프는 n:n) 계층형이고 밑으로 내려가면서 확장되는 거꾸로 나무 모양
* 가장 최상위 노드를 루트라 한다... 반면 가장 끄트머리 노드를 잎(leaf) 노드라 한대 자식이 없는 거지
  헐 간선을 edge라 하는구나
* 차수(degree): 해당노드에 연결된 자식 노드의 수
  그래서 그 트리의 차수: 트리에 있는 노드 차수 중 가장 큰 값
* 높이level: 루트가 0(or 1)의 높이이고 그 밑의 자식은 높이1(or 2) 밑엔 2(or 3) 등 이렇게 내려간다

```python
V = 4  # 정점 갯수
input_string = "1 2 1 3 3 4 3 5"  # 부모 자식 부모 자식 이런 순의 간선들

tree = [[0] for _ in range(V+1)]
array = list(map(int, input().split()))

# 2차원 리스트로

# 첫 번째 방법
for idx in range(len(array)//2):
    parent = array[idx*2]
    child = array[idx**2+1]
    tree[parent].append(child)
    tree[child][0] = parent

#두 번째 방법
tree2 = [[0, 0, 0] for _ in range(V+1)]  # [parent node, child1, child2]
for idx in range(len(array) // 2):
    parent = array[idx*2]
    child = array[idx*2+1]
    if tree[parent][1]:
        tree[parent][2] = child
    else:
        tree2[p][1] = child
        
    tree2[c][0] = parent
```



그럼 트리와 그래프의 차이는? 트리는 뭐가 그렇게 잘났는데?

1. 트리는 순환 구조를 갖지 않는다
2. 루트 노드를 제외한 모든 노드는 부모가 딱 하나
3. 루트 노드는 only one



## 이진트리

* 오 모든 노드가 2개의 서브 트리를 가짐 각각 왼쪽 오른쪽 자식 노드라 하냄
* 이진트리의 노드 최소 갯수는 (높이+1), 최대 갯수는 (2**(높이+1) - 1) (루트높이 0 기준)



 ### 종류

1. 포화 이진 트리 Full Binary Tree
   :모든 노드가 2개씩 꽉꽉 갖고 있는 트리
2. 완전 이진 트리 Complete Binary Tree
   : 음... 최소보다는 크고 최대보다는 작은 개수인데 왼쪽에서부터 꽉꽉 채운 트리
3. 편향 이진 트리 Skewed Binary Tree
   : 오 한쪽 방향의 자식 노드만을 가졌다 그니까 왼쪽 대각선 오른쪽 대각선으로만 그려지는



### 완전 이진 트리의 비밀

노드 번호의 성질

* 노드 번호가 i인 노드의 부모 노드 번호는 i//2
* 노드 번호가 j 인 노드의 왼쪽 자식 노드 번호는 2*j
* 노드 번호가 k인 노트의 오른쪽 자식 노드 번호는 당연히 2*k + 1
* 높이 h의 노드 시작 번호는 2**h



### 순회 Traversal

빠짐 없이, 중복 없이 체계적으로 노드를 방문하는 것

1. 전위 순회 preorder traversal, VLR
   : 부모 노드 방문+처리 &rarr; 자식 노드로 가서 좌, 우 순서로 방문+처리
2. 중위 순회 inorder traversal, LVR
   : ^ 모양으로 가네 왼쪽 자식 &rarr; 부모 노드 &rarr; 오른쪽 자식 노드 순으로 방문+처리
3. 후위 순회 postorder traversal, LRV
   : 자식 노드를 좌, 우 순서로 방문한 후 부모 노드로 방문



#### 전위 순회

하 재귀네...

```python
def 전위순회(부모):
    if 아직 부모가 처리되지 않았다면:
        부모 들러서 처리
        전위순회(왼쪽자식)
        전위순회(오른쪽자식)
```



#### 중위 순회

```python
def 중위순회(부모):
    if 부모가 아직 처리되지 않았다면:
        중위순회(왼쪽자식)
        부모 처리
        중위순회(오른쪽자식)
```



#### 후위 순회

```python
def 후위순회(부모):
    if 부모가 아직 처리되지 않았다면:
        후위순회(왼쪽자식)
        후위순회(오른쪽자식)
        부모 처리
```



### 이진 완전 트리 정보 처리

```python
"""
4  # 간선 갯수
1 2 1 3 3 4 3 5
"""
# 그러므로
for i in range(간선 갯수):
    두 개 들고와서
    if 부모가 비었다면:
        왼쪽 자식에 넣기
    else:  # 부모에 정보가 있다면
        오른쪽 자식에 넣기
```

```python
E = int(input())
array = list(map(int, input().split()))

V = E + 1  # 정점 수 (== 마지막 정점의 번호)

child1 = [0]*(V+1)
child2 = [0]*(V+1)

for i in range(E):
    parent, child = array[i*2], array[i*2+1]  # 두 개씩 끊어서 가져오기
    if child1[parent] == 0:  # 아직 parent의 idx에 해당하는 첫째자식이 비었다면
        child1[parent] = son  # 첫째 자식에
    else:
        child2[parent] = son  # 첫째 자식이 차있다면 둘째 자식에
```

```python
# 자식번호를 인덱스로 해서 그 칸에 부모번호 저장 ㄴㄱ
parent = [0]*(v+1)

for i in range(E):
    p, c = array[i*2], array[i*2+1]
    parent[c] = p
    
# root 찾기
root = 0
for j in range(1, N+1):
    if parent[i] == 0:
        root = i
        break
        
# child번의 조상 찾기
anc = []
while parent[child] != 0:
    anc.append(parent[child])
    child = parent[c]
# 하면 올라갈 때의 모든 조상들을 알려줌
```



## 이진 탐색 트리

모든 원소가 유일한 key를 갖는다
루트가 있으면 왼쪽 자식은 루트보다 작은 키를, 오른쪽 자식은 루트보다 큰 키를 가짐

이렇게 해놓고 중위 순회 하면 오름차순으로 정렬된 값을 얻을 수 있음 그 이진 탐색 그거인 둡

### 탐색연산

1. 키 값 = 해당 노드: 원하는 걸 찾았음
2. 키 값 < 해당 노드: 그 노드의 왼쪽 서브트리에 가서 탐색연산
3. 키 값 > 해당 노드: 그 노드의 오른쪽 서브트리에 가서 탐색연산 맨



## 힙 Heap

1. 완전이진트리에 있는 노드 중에서 
2. 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위한 자료구조
   * max heap: 루트 노드가 가장 큰 키 값 (그렇다고 그 이하가 완전이진트리처럼 정렬된 건 아님)
   * min heap: 루트 노드가 가장 작은 키 값 (마찬가지)

힙에서는 루트 노드의 원소만을 삭제할 수 있다



### ex) 최대 힙

```python
"""
ex. 최대 100의 자연수의 키값, 최대 100개의 정점이 입력된다고 하자
"""
def max_heap(n):
    global last_ver
    last_ver += 1
    tree[last_ver] = n
    # 여기까지 still 완전이진트리
    
    child = last  # 새로 추가된 정점을 자식으로
    parent = child // 2
    
    # 부모가 있고 + 자식의 키값이 부모보다 더 크면
    while p >= 1 and tree[parent] < tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2

tree = [0]*101
last_ver = 0  # 마지막 정점 번호
max_heap(num) # 여러 번 하면 num들이 최대 힙을 유지하면서 사이사이에 들어감
```

```python
# 최대 힙에서 삭제해보자 (삭제는 오직 루트만이)
def del_heap():
    global last_ver
    # 지우기
    temp = tree[1]  # 루트의 key
    tree[1] = tree[last_ver]  # 마지막 정점의 키를 루트에 복사
	last_num -= 1
    
    # 다시 최대힙 되게 재정렬
    parent = 1
    child = parent * 2  # 왼쪽놈 번호
    while child <= last_num:  # 왼쪽 자식이 있다면
        # 오른쪽도 있고 더 크면
        if child+1 <= last_num and tree[child] < tree[child+1]:  
            child += 1  # 오른쪽 놈과 비교하겠어
        if tree[parent] < tree[child]:  # 자식의 키값이 더 크면 슥삭 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            parent = child
            child = parent*2
        else:
            break
    
    return temp

tree = [0]*101
last_ver = 0  # 마지막 정점 번호
del_heap()
```

