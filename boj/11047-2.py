from sys import stdin

N, value = list(map(int, input().split()))
array = []
for i in range(N):
    array.append(int(input()))

count = 0

start = 0
end = N-1

check = -1

if N == 1:
    print(value//N)
else:
    if value > array[-1]:
        for i in range(1, N+1):
            while value > 0:
                value = value - array[-i]
                count += 1
            if value < 0:
                value += array[-i]
                count -= 1
        print(count)
    else:
        while start <= end:
            middle = (start+end) // 2
            if value == array[middle]:
                check = middle
                break
            elif value < array[middle]:
                if array[middle-1] <= value < array[middle]:
                    check = middle-1
                    break
                else:
                    end = middle-1
            elif value > array[middle]:
                start = middle+1

        for i in range(check, -1, -1):
            while value > 0:
                value = value - array[i]
                count += 1
            if value < 0:
                value += array[i]
                count -= 1

        print(count)
