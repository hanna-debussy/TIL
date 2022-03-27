from sys import stdin


def max_heap(n):
    global last_vertex
    last_vertex += 1
    tree[last_vertex] = n

    child = last_vertex  # 새로 추가된 정점을 자식으로
    parent = child // 2

    # 부모가 있고 + 자식의 키값이 부모보다 더 크면
    while parent >= 1 and tree[parent] < tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2


def del_heap():
    global last_vertex
    # 지우기
    root = tree[1]  # 루트의 key
    tree[1] = tree[last_vertex]  # 마지막 정점의 키를 루트에 복사
    tree[last_vertex] = 0
    last_vertex -= 1

    # 다시 최대힙 되게 재정렬
    parent = 1
    child = parent * 2  # 왼쪽놈 번호
    while tree[child] != 0:  # 왼쪽 자식이 있다면
        # 오른쪽도 있고 더 크면
        if tree[child + 1] != 0 and tree[child] < tree[child + 1]:
            child += 1  # 오른쪽 놈과 비교하겠어
        if tree[parent] < tree[child]:  # 자식의 키값이 더 크면 슥삭 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            parent = child
            child = parent * 2
        else:
            break

    return root


N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

tree = [0]*100001
last_vertex = 0

for i in array:
    if i == 0:
        if last_vertex == 0:
            print(0)
        else:
            answer = del_heap()
            print(answer)

    else:
        max_heap(i)
