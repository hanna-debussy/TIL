from sys import stdin

N = int(input())
matrix = [(list(map(int, input().split())), a) for a in range(N)]

div = 1
rank = [0] * N


def body(matrix):
    length = len(matrix)
    global div
    global rank
    bigger = []
    smaller = []

    if length == 0 or length == 1:
        return 0
    else:
        x = matrix[0][0][0]
        y = matrix[0][0][1]
        for i in range(1, length):
            if matrix[i][0][0] > x and matrix[i][0][1] > y:
                bigger.append(matrix[i])
                rank[matrix[i][1]] += 1000/div
            elif matrix[i][0][0] < x and matrix[i][0][1] < y:
                smaller.append(matrix[i])
                rank[matrix[i][1]] -= 1000/div

    div += 1
    big = body(bigger)
    small = body(smaller)

    return 0


result = body(matrix)

final = [[rank[b], b] for b in range(N)]
for n in range(N-1):
    for m in range(n, N):
        if final[n][0] < final[m][0]:
            final[n], final[m]= final[m], final[n]

answer = [0] * N

k = 0
while k < N:
    if k == N-1:
        answer[k] = (k + 1, final[k][1])
        break
    else:
        if final[k][0] > final[k+1][0]:
            answer[k] = (k + 1, final[k][1])
            k += 1
        else:
            answer[k] = (k + 1, final[k][1])
            for z in range(1, N-k):
                if final[k][0] == final[k+z][0]:
                    answer[k+z] = (k + 1, final[k+z][1])
                else:
                    k = k + z
                    break

real = [0]*N
for c in range(N):
    real[answer[c][1]] = answer[c][0]

print(*real)
