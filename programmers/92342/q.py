# 양궁대회
# 2022 카카오 블라인드 채용 level2
import functools


def solution(n, info):
    cache = [[False] * 11 for _ in range(n + 1)]

    def re(index, remain_shots):
        nonlocal cache, info

        if index > 10:
            return 0

        if cache[remain_shots][index] != False:
            return cache

        ret = -9999
        if info[index] + 1 <= remain_shots:
            temp = 10 - index
            mx = temp + re(index + 1, remain_shots - info[index] - 1)
            ret = max(mx, ret)

        if info[index] > 0:
            temp = 10 - index
            mx = -temp + re(index + 1, remain_shots)
            ret = max(mx, ret)
        else:
            mx = re(index + 1, remain_shots)
            ret = max(mx, ret)

        return ret

    state = [0] * 11

    def reconstruct(remains, index, state):
        if index > 10:
            return

        if info[index] + 1 <= remains:
            if re(remains, index + 1) == re(remains - info[index] - 1, index + 1):
                reconstruct(remains, index + 1, state)
            else:
                state[index] = info[index] + 1
                reconstruct(remains - info[index] - 1, index + 1, state)
        else:
            reconstruct(remains, index + 1, state)

    reconstruct(n, 0, state)
    return state


def test_1():
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    ans = [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]

    answer = solution(n, info)
    assert ans == answer
