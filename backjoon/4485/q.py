# 녹색 옷 입은 애가 젤다지?
import math
from collections import defaultdict

DIR = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]


def solution(cave):
    global N
    connection = defaultdict(dict)
    adj = [[math.inf for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            pos = (y, x)
            idx = y * N + x
            for i in range(4):
                ny, nx = (pos[0] + DIR[i][0], pos[1] + DIR[i][1])
                if 0 <= ny < N and 0 <= nx < N:
                    nxt_idx = ny * N + nx
                    connection[idx][nxt_idx] = cave[ny][nx]
                    connection[nxt_idx][idx] = cave[y][x]


if __name__ == "__main__":
    C = int(input())
    N = int(input())
    for c in range(C):
        cave = []
        for i in range(N):
            temp = input().split(" ")
            cave.append([map(int, temp)])
