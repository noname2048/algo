# 누적합 이용해보기
import math
import sys

sys.stdin = open("p1.txt", "r")
input = sys.stdin.readline


def main():
    n, k, l = list(map(int, input().split()))
    m = list(map(int, input().split()))
    t = list(map(int, input().split()))

    cola_array = [0] * n
    for ti in t:
        cola_array[ti - 1] += 1

    acum = cola_array.copy()
    for i in range(1, n):
        acum[i] = acum[i] + acum[i - 1]

    effect = [0] * n
    for i in range(n):
        if i - 1 < 0:
            effect[i] = acum[i]
        else:
            effect[i] = acum[i] - acum[i - l]

    cola = list(map(lambda x: [x[1], x[0]], enumerate(effect)))
    cola.sort(reverse=True)
    m.sort(reverse=True)

    max_cap = 0
    for i in range(n):
        max_cap += math.floor(m[i] / (2 ** cola[i][0]))
    print(max_cap)


main()
