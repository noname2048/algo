from typing import List, Tuple
import sys
from collections import deque
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


def solution(n: int, vectors: List[Tuple[int]]) -> float:
    used = {}
    for i in range(n):
        used[i] = False

    def dfs():
        unused = [k for k, v in used.items() if v == False]
        if len(unused) == 0:
            return 0

        idx, origin_y, origin_x = unused[0]

        local_min = math.inf
        local_min_idx = 0

        for i in range(1, len(unused)):
            next, py, px = unused[i]
            distance = (origin_y - py) ^ 2 + (origin_x - px) ^ 2
            if local_min > distance:
                local_min = distance
                local_min_idx = next

        used[idx] = True
        used[local_min_idx] = True

        return dfs() + local_min

    return dfs()


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        vectors = []
        for i in range(n):
            py, px = map(int, input().split(" "))
            vectors.append((i, py, px))
        ans = solution(n, vectors)
        print(ans)
