from sys import stdin

N = int(input())

parents = []
children1 = []
children2 = []
for _ in range(N):
    p, c1, c2 = list(input().split())
    parents.append(p)
    children1.append(c1)
    children2.append(c2)


pre = []
ino = []
post = []


def preorder(chr):
    pre.append(chr)
    for i in range(N):
        if chr == parents[i]:
            if children1[i] != ".":
                preorder(children1[i])
            if children2[i] != ".":
                preorder(children2[i])


def inorder(chr):
    for i in range(N):
        if chr == parents[i]:
            if children1[i] != ".":
                inorder(children1[i])
    ino.append(chr)
    for j in range(N):
        if chr == parents[j]:
            if children2[j] != ".":
                inorder(children2[j])


def postorder(chr):
    for i in range(N):
        if chr == parents[i]:
            if children1[i] != ".":
                postorder(children1[i])
            if children2[i] != ".":
                postorder(children2[i])
    post.append(chr)


preorder("A")
for x in pre:
    print(x, end="")
print()

inorder("A")
for y in ino:
    print(y, end="")
print()

postorder("A")
for z in post:
    print(z, end="")

"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""