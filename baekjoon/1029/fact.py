import math


def factorial(n):

    # cache[node_idx][visit]
    bit_space = int("1" * n, 2) + 1
    cache = [[-1] * bit_space for _ in range(n)]
    cnt = 0

    def re(here, visit, path):
        nonlocal cnt

        if cache[here][visit] >= 0:
            cnt += 1
            # print(f"{cnt:03d}", path)
            return cache[here][visit]

        if visit == bit_space - 1:
            cnt += 1
            # print(f"{cnt:03d}", path)
            return 0

        result = [0]
        for next in range(n):
            if visit & 1 << next:
                continue

            tmp = re(next, visit | 1 << next, path + [next + 1])
            result.append(tmp)

        cache[here][visit] = max(result) + 1
        return cache[here][visit]

    ans = re(0, 1, [1])
    # print(ans + 1)
    return ans, cnt


if __name__ == "__main__":
    for node in range(4, 15):
        ans, cnt = factorial(node)
        f = math.factorial(node - 1)
        print(node, f, cnt, cnt / f * 100)

"""
4 6 6 100.0
5 24 24 100.0
6 120 90 75.0
7 720 300 41.66666666666667
8 5040 910 18.055555555555554
9 40320 2576 6.388888888888888
10 362880 6930 1.9097222222222223
11 3628800 17940 0.49437830687830686
12 39916800 45078 0.11292989417989417
13 479001600 110616 0.023093033509700177
14 6227020800 266266 0.004275977366255144
"""
