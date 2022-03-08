from sys import stdin

N = int(input())
array = list(map(int, input().split()))

sub_list = []
last = 0
count = 0
if len(array) == 1:
    print(1)
else:
    for i in range(N-1):
        if array[i] < array[i+1]:
            count += 1
            if count == 1:
                sub_list.append(array[i])
            sub_list.append(array[i+1])
    answer = len(sub_list)
    print(answer)

# 9
# 30 10 20 2 5 10 20 30 50
# 
# 9
# 8 30 10 20 30 40 2 5 50
# 경우에 안 됨