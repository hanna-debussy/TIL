from sys import stdin

N, M, V = list(map(int, input().split()))
rename_temp = []
edges = []
for _ in range(M):
    temp = list(map(int, input().split()))
    rename_temp.append(temp[0])
    rename_temp.append(temp[1])
    edges.append(temp)

rename_list = list(set(rename_temp))
new_idx = sorted(rename_list)
dicts = {}
for idx, val in enumerate(new_idx):
    dicts[val] = idx

# print(dicts)
matrix = [[0]*len(new_idx) for _ in range(len(new_idx))]

for edge in edges:
    matrix[dicts[edge[0]]][dicts[edge[1]]] = 1
    matrix[dicts[edge[1]]][dicts[edge[0]]] = 1

# print(matrix)


# DFS
stack_d = []
to_visit = [dicts[V]]
whole = len(new_idx)
while len(stack_d) < whole:
    if to_visit[-1] in stack_d:
        to_visit.pop()
    elif to_visit[-1] not in stack_d:
        go = to_visit.pop()
        stack_d.append(go)
        for i in range(whole-1, -1, -1):
            if matrix[go][i] == 1:
                to_visit.append(i)

result_d = []
for sd in stack_d:
    for idx, value in dicts.items():
        if sd == value:
            result_d.append(idx)

print(*result_d)


# BFS
stack_b = []
to_go = [dicts[V]]

while len(stack_b) < whole:
    if to_go[0] in stack_b:
        to_go.pop(0)
    elif to_go[0] not in stack_b:
        go = to_go.pop(0)
        stack_b.append(go)
        for i in range(whole):
            if matrix[go][i] == 1:
                to_go.append(i)

result_b = []
for sd in stack_b:
    for idx, value in dicts.items():
        if sd == value:
            result_b.append(idx)

print(*result_b)
