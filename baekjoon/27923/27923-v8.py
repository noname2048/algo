# max -> min 으로 교체후 풀이 완료
from itertools import accumulate
import math
import sys

sys.stdin = open("p5.txt", "r")
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
    for i in range(min(l, n)):
        effect[i] = cola_array[i]
    for i in range(l, n):
        effect[i] = cola_array[i] - cola_array[i - l]

    effect.sort(reverse=True)
    m.sort(reverse=True)

    caps = [math.floor(m[i] / (2**effect[i])) for i in range(n)]
    answer = sum(caps)
    print(answer)


main()
