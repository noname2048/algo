# 녹색 옷 입은 애가 젤다지?
import math
from collections import defaultdict

DIR = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]


def solution(N, cave):
    mx = math.inf
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True

    def dfs(pos, value):
        global DIR
        nonlocal cave, visited, mx
        if pos == (N - 1, N - 1):
            mx = min(mx, value)
            return

        if value > mx:
            return

        for i in range(4):
            ny, nx = pos[0] + DIR[i][0], pos[1] + DIR[i][1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs((ny, nx), value + cave[ny][nx])
                visited[ny][nx] = False

    dfs((0, 0), cave[0][0])
    return mx


def predata():
    def make_gen():
        yield from """3
        5 5 4
        3 9 1
        3 2 7
        5
        3 7 2 0 1
        2 8 0 9 1
        1 2 1 8 1
        9 8 9 2 0
        3 6 5 1 5
        7
        9 0 5 1 1 5 3
        4 1 2 1 6 5 3
        0 7 6 1 6 8 5
        1 1 7 8 3 2 3
        9 4 0 7 6 4 1
        5 8 3 2 4 8 3
        7 4 8 4 8 3 4
        0""".splitlines()

    gen = make_gen()

    def get_iter():
        nonlocal gen
        return next(gen)

    return get_iter


if __name__ == "__main__":
    # input = predata()
    N = int(input())
    while N != 0:
        cave = []
        for i in range(N):
            temp = input().strip().split(" ")
            cave.append(list(map(int, temp)))

        ans = solution(N, cave)
        print(ans)

        N = int(input())
