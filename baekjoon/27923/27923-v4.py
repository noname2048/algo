# v3 에 비해 꽤 줄인 거 같은데 잘 안됨
# 뭐가 문제일까?
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

    effect.sort(reverse=True)
    m.sort(reverse=True)

    caps = [math.floor(mi / (2**ei)) for mi, ei in zip(m, effect)]
    answer = sum(caps)
    print(answer)


main()
