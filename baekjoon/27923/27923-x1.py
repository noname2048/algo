# https://www.acmicpc.net/source/58468972
from itertools import accumulate
import sys

sys.stdin = open("p1.txt")

N, K, L = [int(item) for item in input().split(" ")]
hambuergers = [int(item) for item in input().split(" ")]
colas = [0] * N
for i in map(int, input().split()):
    colas[i - 1] += 1
    colas[min(i - 1 + L, N - 1)] -= 1
colas = sorted(accumulate(colas))
ans = sum(h // (1 << t) for h, t in zip(hambuergers, colas) if t < 64)
print(ans)
