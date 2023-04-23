# pypy3 -> wrong
from itertools import accumulate
import math
import sys

sys.stdin = open("p2.txt", "r")
input = sys.stdin.readline


def main():
    n, k, l = list(map(int, input().split()))
    m = list(map(int, input().split()))
    t = list(map(int, input().split()))

    cola_array = [0] * n
    for ti in t:
        cola_array[ti - 1] += 1

    cola_array = list(accumulate(cola_array))

    effect = [0] * n
    for i in range(l):
        effect[i] = cola_array[i]
    for i in range(l, n):
        effect[i] = cola_array[i] - cola_array[l]

    effect.sort(reverse=True)
    m.sort(reverse=True)

    caps = [math.floor(mi / (2**ei)) for mi, ei in zip(m, effect)]
    answer = sum(caps)
    print(answer)


main()
