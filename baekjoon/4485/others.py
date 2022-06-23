from sys import stdin
from heapq import *

input = stdin.readline


def solve():

    problem = 1
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        N = int(input())
        if N == 0:
            return
        arr = [list(map(int, input().split())) for _ in range(N)]
        h = []
        heappush(h, (arr[0][0], (0, 0)))
        visited = [[False] * N for _ in range(N)]
        target = (N - 1, N - 1)
        while True:
            cost, pos = heappop(h)
            if pos == target:
                print("Problem %d: %d" % (problem, cost))
                problem += 1
                break
            nx, ny = pos
            for dx, dy in d:
                x, y = nx + dx, ny + dy
                if 0 <= x < N and 0 <= y < N:
                    if not visited[x][y]:
                        heappush(h, (arr[x][y] + cost, (x, y)))
                        visited[x][y] = True


solve()
