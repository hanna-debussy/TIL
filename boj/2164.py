from sys import stdin

N = int(input())

array = [i for i in range(N, 0, -1)]

while len(array) > 1:
    array.pop()
    temp = array.pop()
    array = [temp] + array
    print(array)
print(*array)