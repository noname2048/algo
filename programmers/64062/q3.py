# 이분법


def solution(stones, k):
    highest_able = min(stones)
    lowest_unable = max(stones)

    lo = highest_able
    hi = lowest_unable
    mi = (lo + hi + 1) // 2

    def cond():
        return lowest_unable - highest_able == 1

    while not cond():
        continus_zero = 0

        for s in stones:
            if s - (mi - 1) <= 0:
                continus_zero += 1
            else:
                continus_zero = 0

            if continus_zero >= k:
                lowest_unable = mi
                hi = mi - 1
                mi = (lo + hi + 1) // 2
                break
        else:
            highest_able = mi
            lo = mi + 1
            mi = (lo + hi + 1) // 2

    return highest_able


def test_1():
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    ans = solution(stones, k)
    assert ans == 3


test_1()
