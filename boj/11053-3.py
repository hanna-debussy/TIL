from sys import stdin

N = int(input())
array = list(map(int, input().split()))


# LIS
def lis(arr):
    if not arr:
        return 0

    max_count = 1  # 원소는 하나는 들어있다는

    """
    이 다음이 중요한데 모든 증가부분 수열을 훑는 방법이기 때문에
    어떤 수라도 수열의 처음이 될 수 있다
    그러므로 증가수열의 가장 첫 수를 세팅해주는 게 첫 for문이다
    """
    for i in range(len(arr)):
        # 처음 수 i에서부터 만든 증가수열을 넣을 곳
        next = []
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next.append(arr[j])
        """
        ret이 우리가 구할 답인디 여기에 아까 수열이랑 지금 수열을 비교하는데
        1을 더하는 이유가 지금 우리가 만든 건 앞서 만든 거에서 하나 추가한 것이기 때문에
        지금 우리는 수열 자체를 구하는 게 아니라 숫자만 세면 되니까 이렇게 구하는 것
        """
        max_count = max(max_count, 1+lis(next))
    return max_count


answer = lis(array)
print(answer)
