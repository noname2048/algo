# https://www.acmicpc.net/source/58192652
# 위의 코드 참조
# 단순 반복 버전인 것 같은데 pypy3 로 제축하더니 엄청 빠른 결과를 보여준다.

import sys

sys.stdin = open("p3.txt", "r")
input = lambda: sys.stdin.readline().rstrip()

from itertools import product

INF = 1 << 60
STATES = list(product(range(10), range(10), range(10)))
COST = [[0, 1, 2, 3, 4, 5, 4, 3, 2, 1]]
for i in range(9):
    COST.append(COST[i][9:] + COST[i][:9])


def main():
    N = int(input())
    li = list(map(int, input().split()))

    x = [COST[0][i] + COST[0][j] + COST[0][k] for i, j, k in STATES]
    ind = lambda i, j, k: i * 100 + j * 10 + k

    for e in li:
        y = [INF for i in range(1000)]
        for i, j, k in STATES:
            y[ind(e, j, k)] = min(y[ind(e, j, k)], x[ind(i, j, k)] + COST[i][e])
            y[ind(i, e, k)] = min(y[ind(i, e, k)], x[ind(i, j, k)] + COST[j][e])
            y[ind(i, j, e)] = min(y[ind(i, j, e)], x[ind(i, j, k)] + COST[k][e])
        x = y

    ans = INF
    for i in x:
        if i != -1:
            ans = min(ans, i)

    print(ans)


if __name__ == "__main__":
    main()
