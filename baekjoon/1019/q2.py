"""
일의 자리 수에서 1 보다 크면 1 에 10의 자리수 마다 반복
십의 자리 수에서 10 ~ 19 까지 + 10
백의 자리 수에서 100 ~ 199 까지  + 100
천의 자리 수에서 1000 ~ 1999 까지  + 1000

2를 가지고 해보자
일의 자리 수에서 2보다 크면 1
십의 자리 수에서 20~29 까지  + 10
...

0은 좀 다를거야
일의 자리수에서 10으로 나눈 몫 마다 + 1
십의 자리 수에서 100 ~ 109 까지 추가로 0이 10개 추가
백의 자리 수에서 1000 ~ 1099까지 추가로 0이 100개 추가
"""

from re import I


def calc(n, target):
    length = len(str(n))

    k = 0
    for i in range(length):
        unit = pow(10, i)
        q, r = divmod(n, unit * 10)
        k += q * unit
        if r >= (target + 1) * unit:
            k += unit
        elif r >= target * unit:
            k += r - target * unit + 1

    return k


"""
0이 좀 어렵네
10으로 나눠서 몫이 나오면 그만큼 더하기
100으로 나눠서 몫이 나오면 110까지 계산하기
1000으로 나눠서 몫이 나오면 1100까지 계산하기

105 
10 20 30 ... 90 100 중 일의자리 (10개)
100 ~ 105 까지 십의자리 6개
"""


def calc2(n):
    length = len(str(n))

    k = 0
    for i in range(length):
        unit = pow(10, i)
        q, r = divmod(n, unit * 10)
        k += (q - 1) * unit
        if r >= 1 * unit:
            k += unit
        else:
            k += r + 1

    return k


def solve(n=None):
    if not n:
        n = int(input())
    ans = [calc2(n)]
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        ans.append(calc(n, i))

    print(" ".join(map(str, ans)))
    return ans


def test_solve():
    ns = [11, 7, 19, 199]
    ans = [
        [1, 4, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 12, 2, 2, 2, 2, 2, 2, 2, 2],
        [
            189,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
        ],
        [
            429904664,
            541008121,
            540917467,
            540117067,
            533117017,
            473117011,
            429904664,
            429904664,
            429904664,
            429904664,
        ],
    ]
    for i in range(4):
        an = solve(ns[i])
        assert (an, ans[i])


if __name__ == "__main__":

    solve(11)
    solve(7)
    solve(19)
