from collections import defaultdict
import math
import heapq

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(N, cave):
    graph = defaultdict(defaultdict)
    # 다익스트라로 풀기
    # 1. 그래프 만들기
    graph = defaultdict(dict)
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny, nx = y + DIR[i][0], x + DIR[i][1]
                if 0 <= ny < N and 0 <= nx < N:
                    pos = (y, x)
                    nxt_pos = (ny, nx)

                    graph[pos][nxt_pos] = cave[ny][nx]
                    graph[nxt_pos][pos] = cave[y][x]
    # 2. 다익스트라
    start_pos = (0, 0)
    dist = defaultdict(lambda: math.inf)
    visit = defaultdict(lambda: False)
    heap = [(0, start_pos)]
    dist[start_pos] = 0

    while heap:
        value, pos = heapq.heappop(heap)
        visit[pos] = True

        if value == math.inf:
            continue

        near = graph[pos]
        for k, v in near.items():
            if k != start_pos and dist[pos] + graph[pos][k] < dist[k]:
                dist[k] = dist[pos] + graph[pos][k]

            if k not in visit:
                heapq.heappush(heap, (v, k))

    return dist[(N - 1, N - 1)] + cave[0][0]


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
    while N != 0:
        cave = []
        for i in range(N):
            temp = input().strip().split(" ")
            cave.append(list(map(int, temp)))
        ans = solution(N, cave)
        print(ans)

        N = int(input())
