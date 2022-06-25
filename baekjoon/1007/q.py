import sys
import math


def get_custom_input():
    with open("./data.txt", "r") as f:
        lines = f.readlines()
        lines = map(lambda s: s.strip(), lines)

    def my_gen():
        with open("data.txt", "r") as f:
            lines = f.readlines()
        yield from lines

    gen = my_gen()

    def my_iter():
        nonlocal gen
        return next(gen)

    return my_iter


# input = sys.stdin.readline
input = get_custom_input()


def solution(n, vectors) -> float:
    half = n // 2
    used = [False] * len(vectors)
    min_distance = math.inf

    def comb(depth, start, index_choice):
        nonlocal min_distance, half, n
        if depth == half:
            minus = set(index_choice)
            plus = set(range(0, n)) - minus

            my, mx = 0, 0
            for k in minus:
                my += vectors[k][0]
                mx += vectors[k][1]
            py, px = 0, 0
            for k in plus:
                py += vectors[k][0]
                px += vectors[k][1]

            distance = (py - my) ** 2 + (px - mx) ** 2
            if min_distance > distance:
                min_distance = distance
            return

        remain = half - depth
        for i in range(start, n - remain + 1):
            comb(depth + 1, i + 1, index_choice + [i])

    comb(0, 0, [])
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
