# 에라토스테네스의 체를 이용하기
from sys import stdin

input = stdin.readline


def solve():
    mn, mx = map(int, input().split())
    cache = [False] * (mx - mn + 1)

    i = 2
    j = i**2
    while j <= mx:

        k = j
        while k <= mx:
            if k - mn >= mn:
                cache[k - mn] = True
            k += j

        i += 1
        j = i**2

    cnt = 0
    for i in range(mn, mx + 1):
        if cache[i - mn] == False:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    solve()
