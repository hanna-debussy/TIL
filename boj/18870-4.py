from sys import stdin

N = int(input())
array = list(map(int, input().split()))

sorted_array = sorted(list(set(array)))

sorted_dict = {}

for idx, k in enumerate(sorted_array):
    sorted_dict[k] = idx

answer = []

for i in array:
    answer.append(sorted_dict[i])

print(*answer)
