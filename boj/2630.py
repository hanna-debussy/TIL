from sys import stdin

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

one = 0
zero = 0


def origami(N, r, c):
    # # n = int(n)
    # r = int(r)
    # c = int(c)
    global zero
    global one
    temp_zero = 0
    temp_one = 0
    for i in range(N):
        for j in range(N):
            if matrix[r+i][c+j] == 0:
                temp_zero += 1
            else:
                temp_one += 1
    if temp_one == N**2:
        one += 1
    elif temp_zero == N**2:
        zero += 1
    else:
        N = N//2
        for a in range(2):
            for b in range(2):
                origami(N, r+(a*N), c+(b*N))


origami(N, 0, 0)
print(zero, one)