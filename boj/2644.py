from sys import stdin

N = int(input())
targets = list(map(int, input().split()))
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(M)]

edges = [[] for _ in range(N)]

for i in range(M):
    edges[matrix[i][0]].append(matrix[i][1])

count = 0


def inorder(n):
    global count

    parent = -1
    count += 1
    for j in matrix:
        if j[1] == n:
            parent = j[0]

    if parent == targets[1]:
        return
    else:
        for k in edges[parent]:     # parent의 자식들에 대해
            if k == targets[1]:     # 자식들이 찾고자 하는 타겟이면
                if k != n:          # 대신 출발했던 자식은 아니어야 하고
                    count += 1
                    return
            elif k != targets[1]:
                if k != n and edges[k-1] != []:
                    for x in edges[k]:
                        inorder(x)
        check = 0
        for l in matrix:
            if parent == l[1]:
                check += 1
        if check == 0:
            count = -1
            return
        else:
            inorder(parent)


inorder(targets[0])
print(count)
"""
9
7 8
7
1 2
1 3
2 7
3 8
2 9
4 5
4 6
"""