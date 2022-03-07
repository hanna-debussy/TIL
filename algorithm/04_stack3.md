# 03. Stack

필기를 안 옮겼네



## 조합

```python
def perm(i):
    # base case(탐색중인 idx가 length와 같다 == 탐색 끝)
    if i == N:
        print(*numbers)
        return

    # 제자리 그대로 부터, 마지막 idx까지
    for j in range(i, N):
        numbers[i], numbers[j] = numbers[j], numbers[i]
        perm1(i+1)
        numbers[i], numbers[j] = numbers[j], numbers[i]


numbers = [1, 2, 3]
N = len(numbers)

perm(0)
```

