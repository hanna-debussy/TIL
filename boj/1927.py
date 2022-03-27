import sys


def min_heap(n):
    global last_vertex, tree
    if len(tree) - 1 == last_vertex:
        tree = tree + [float("inf")]*(len(tree))

    last_vertex += 1
    tree[last_vertex] = n

    child = last_vertex
    parent = child // 2

    while parent >= 1 and tree[child] < tree[parent]:
        tree[child], tree[parent] = tree[parent], tree[child]
        child = parent
        parent = child // 2


def del_heap():
    global last_vertex

    root = tree[1]
    tree[1] = tree[last_vertex]
    tree[last_vertex] = float("inf")
    last_vertex -= 1

    parent = 1
    child = parent*2
    while child < len(tree) and tree[child] == float("inf"):
        if tree[child+1] != float("inf") and tree[child] > tree[child+1]:
            child += 1
        if tree[child] < tree[parent]:
            tree[child], tree[parent] = tree[parent], tree[child]
            parent = child
            child = parent*2
        else:
            break

    return root


N = int(input())
last_vertex = 0
tree = [float("inf")]

for i in range(N):
    a = int(input())
    if a == 0:
        if last_vertex == 0:
            print(0)
        else:
            answer = del_heap()
            print(answer)
    else:
        min_heap(a)
