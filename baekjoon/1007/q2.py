import sys
from itertools import combinations
import math

input = sys.stdin.readline


def solution(n, vectors):
    domain = list(range(len(vectors)))
    half = len(vectors) // 2
    comb = combinations(domain, half)
    min_distance = math.inf

    for c in comb:
        minus = set(c)
        plus = set(domain) - minus
        my, mx = 0, 0
        py, px = 0, 0
        for i in minus:
            my += vectors[i][0]
            mx += vectors[i][1]
        for i in plus:
            py += vectors[i][0]
            px += vectors[i][1]

        distance = (py - my) ** 2 + (px - mx) ** 2
        if min_distance > distance:
            min_distance = distance

    return math.sqrt(min_distance)


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        vectors = []
        for i in range(n):
            py, px = map(int, input().split(" "))
            vectors.append([py, px])
        ans = solution(n, vectors)
        print(ans)
