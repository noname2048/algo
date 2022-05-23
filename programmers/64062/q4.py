# other 보고 좀더 간결하게


def solution(stones, k):
    ans, left, right = -1, min(stones), max(stones)

    while left <= right:
        mid = (left + right) // 2
        continus_zero = 0

        for s in stones:
            if s - mid < 0:
                continus_zero += 1
            else:
                continus_zero = 0

            if continus_zero >= k:
                right = mid - 1
                break
        else:
            ans = mid
            left = mid + 1

    return ans
