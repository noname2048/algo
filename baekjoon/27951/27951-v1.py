# 3660ms 맞았습니다 (헉)

import sys

sys.stdin = open("p3.txt", "r")
input = lambda: sys.stdin.readline().strip()


def thousand2abc(n):
    return n // 100, (n % 100) // 10 % 10, n % 10


def abc2thousand(a, b, c):
    return a * 100 + b * 10 + c


def dist(u, v):
    return min(abs(u - v), 10 - abs(u - v))


def get_new_status(current, number):
    a, b, c = thousand2abc(current)
    new_status = [
        abc2thousand(number, b, c),
        abc2thousand(a, number, c),
        abc2thousand(a, b, number),
    ]
    return new_status


def main():
    n = int(input())
    t = list(map(int, input().split()))

    # 그리디로 풀 수 있는 점화식 발견 실패
    # dp 나 탐색에서 수를 줄일 수 있는 방안으로

    cache = [[-1] * 1000 for _ in range(n)]

    k = t[0]
    d = dist(0, k)
    cache[0][abc2thousand(k, 0, 0)] = d # 무조건 첫번째 화구 사용

    for n_idx in range(1, n):
        for status_idx in range(1000):
            # 이전 결과값 없음
            if cache[n_idx - 1][status_idx] == -1:
                continue

            current_abc = thousand2abc(status_idx)
            new_status = get_new_status(status_idx, t[n_idx])

            for i in range(3):
                next_status = new_status[i]
                d = dist(current_abc[i], t[n_idx])
                if cache[n_idx][next_status] == -1:  # 결과값 없음
                    cache[n_idx][next_status] = cache[n_idx - 1][status_idx] + d
                else:  # 최소 결과값 status_idx
                    cache[n_idx][next_status] = min(
                        cache[n_idx][next_status], cache[n_idx -1][status_idx] + d
                    )

    ## for debug
    # with open("log.txt", "w") as f:
    #     for i in range(n):
    #         f.write(f"{i:02d}회차---\n")
    #         for j in range(1000):
    #             if cache[i][j] != -1:
    #                 f.write(f"{j:03d} -- \t{cache[i][j]}\n")

    answer = 90_000
    for i in range(1000):
        if cache[n - 1][i] != -1:
            answer = min(answer, cache[n - 1][i])

    print(answer)


main()
