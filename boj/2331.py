import sys

first, power = map(int, input().split())

array = [first]

while True:
    last = array[-1]
    separated = list(map(int, str(last)))
    next = 0
    for s in separated:
        next += s**power

    if next in array:
        idx = array.index(next)
        print(idx)
        break

    array.append(next)
