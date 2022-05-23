# 징검다리 건너기


def solution(stones, k):
    for j in range(200_000_000):
        continus_zero = 0
        for i, s in enumerate(stones):
            if s <= 0:
                continus_zero += 1
            else:
                continus_zero = 0

            stones[i] -= 1

            if continus_zero >= k:
                return j


def test_1():
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    ans = solution(stones, k)
    assert ans == 3


test_1()
