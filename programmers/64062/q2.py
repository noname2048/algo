# 슬라이딩 윈도우로 풀어보자


def solution(stones, k):
    ls = len(stones)
    mn = 200_000_000
    for i in range(ls - k + 1):
        window = stones[i : i + k]
        temp = max(window)
        mn = min(temp, mn)

    return mn


def test_1():
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    ans = solution(stones, k)
    assert ans == 3


test_1()
