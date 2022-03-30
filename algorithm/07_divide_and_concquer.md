# 6. 분할정복

![img](https://mblogthumb-phinf.pstatic.net/MjAyMDAyMTZfMjk1/MDAxNTgxNzgyMDE5NTQ2.Cu3jV-ue-2aZa_wfw9Av7AfnE7fT6jcrkzu4_BWknmMg.00IlVkIpgQ_giqwYrFkLZYxWo7SlZQhtdQwGcqC1_kAg.PNG.woqls22/image.png?type=w800)

따로따로따로 부분부분부분 하고 그걸 합쳐합쳐합쳐 (???)



## 병합 정렬 Merge Sort

분할정복의 한 종류인데... 전체 자료 집합에 대해 최소 크기의 부분집합이 될 때까지 분할을 계속함

1. 정렬하고자 하는 애들을 절반절반절반 해서 한 개가 될 때까지 잘라
2. 두 개의 부분집합을 정렬+병합한다.  인덱스 순서대로 두개씩 잘라서 두 개를 비교함
3. 아 근데 비교하는 방법이 신기하다 만약 네 개 네 개 두 개가 만났어 그러면 1-1과 2-1을 비교하고 1-1은 1-2로 넘어가 그리고 1-2와 2-1을 비교하고 1-2가 작으면 1-2 넣고 1-3으로 넘어가 그리고 1-3과 2-1 비교해서 2-1을 넣고 2-2로 넘어가고... 이렇게 된다

단점은 메모리가 많이 쓰인다



### 알고리즘

```python
def m_s(array):
    if len(array) == 1:
        return array
    
    left, right = [], []
    middle = len(array) // 2
    for x in array[0]~middle:
        add x to left
    for y in middle~array[-1]:
        add x to right
    
    merge(left)
    merge(right)
    
    return left+right


def merge(left, right):
    result = []
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                
    return result
```



## 퀵 정렬

얘도 배열을 두 개로 짜개서 각각을 정렬하는 방법이다. 하지만 병합 정렬이랑 같은 건 아님

1. 퀵 정렬은 쪼갤 때 pivot을 기준으로 이거보다 작으면 앞에, 크면 뒤에 놓음
2. 병합은 끝나고 병합이라는 마지막 작업이 필요하지만 퀵정렬은 그냥 쨘



### 알고리즘

```python
def q_s(array, l, r):
    if l < r:
        s = partition(array, l, r)
        q_s(array, l, s-1)
        q_s(array, s+1, r)
        

# Hoare-partition algorithm
def partition(array, left, right):
    pivot = array[left]
    i, j = left, rhght
    while i <= j:
        while i <= j and array[i] <= pivot:  # left에서는 작으면 그냥 넘김
            i += 1
        while i <= j and array[j] >= pivot:  # right에서는 크면 그냥 넘김
            j -= 1
        if i < j:  # left에서 피봇보다 큰 애랑 right에서 피봇보다 작은 애에서 걸리면
            array[i], array[j] = array[j], array[i]  # 둘이 자리를 바꿔줌
    
    array[l], array[j] = array[j], array[l]
    
    return j
```



피봇은 그럼 어케 선택하느냐?
&rarr; [0], [middle], [-1] 중에서 중간값을 보통 고른대



오 또 다른 알고리즘이 있네... 알고리즘 멈춰!

```python
#Lomuto partition algorithm

def partition(array, pivot, right):
    x = array[r]  # 얘가 pivot이 된다
    i = p - 1
    
    for j in range(p, r):  # j는 r-1까지 쭉 가는데
        if array[j] <= x:  # pivot보다 작으면
            i += 1  # 한 칸 넘어가
            # 그리고 바꿔주...는데 이게 j랑 1 커진 i는 같은 자리라서 나랑 나를 바꾸는 셈
            array[i], array[j] = array[j], array[i]
   			"""
            그 말은 뭐냐면 pivot보다 큰 애를 만나면 i는 멈춤
            그리고 작은 애 만나면 그제야 걔랑 나를 바꿔서 큰 애를 뒤로 보냄
            그러다보면 피봇보다 큰 애에 i가, 피봇(가장 오른쪽)에 j가 되면서
            둘이 슥삭해서 피봇이 그 기준에 자리잡게 됨 배앰
            """
   	array[i+1], array[r] = array[r], array[i+1]
    
    return i+1
```



## 이진검색 Binary Search

분할정복 왜케... 광범위하게 쓰이냐

**이진 검색 하려면 자료가 정렬된 상태여야 한다**
자료의 가운데에 있는 값과 비교하고 다음 검색의 위치를 결정 < 을 반복하다보면 검색 범위를 반반반으로 줄여나갈 수 있어서 빠르게 정렬이 가능하다

이거는 머... 알지? 중간보다 작으면 end를 middle-1로 옮기고 중간보다 크면 start를 middle+1로 옮기는 거 rgrg