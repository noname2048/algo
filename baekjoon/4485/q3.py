import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def solution(N, cave):
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = cave[0][0]
    dirx = [1, 0, -1, 0]
    diry = [0, 1, 0, -1]
    q = []

    heapq.heappush(q, (cave[0][0], 0, 0))
    while q:
        value, y, x = heapq.heappop(q)

        if distance[y][x] < value:
            continue

        for i in range(4):
            ny = y + diry[i]
            nx = x + dirx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if value + cave[ny][nx] < distance[ny][nx]:
                    distance[ny][nx] = value + cave[ny][nx]
                    heapq.heappush(q, (value + cave[ny][nx], ny, nx))

    return distance[-1][-1]


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
    input = predata()
    N = int(input())
    problem_number = 1
    while N != 0:
        cave = []
        for i in range(N):
            temp = input().strip().split(" ")
            cave.append(list(map(int, temp)))
        ans = solution(N, cave)
        print(f"Problem {problem_number}: {ans}")

        problem_number += 1
        N = int(input())
