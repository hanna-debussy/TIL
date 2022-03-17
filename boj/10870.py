from sys import stdin

N = int(input())

fib = [0, 1]

for i in range(2, N+1):
    nth = fib[i-1] + fib[i-2]
    fib.append(nth)
print(fib[N])
