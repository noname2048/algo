import sys
from collections import defaultdict

# sys.stdin = open("input1.txt", "r")
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(idx):
    if dp_cache[idx]:
        return dp_cache[idx]

    value = 0
    next_cave = 0
    for b, c in connect[idx]:
        cost = dfs(b) - c
        if cost >= value:
            value = cost
            next_cave = b

    dp_cache[idx] = value + cave[idx]
    dp_path_cache[idx] = next_cave
    return dp_cache[idx]


tc = int(input())  # test_case
for _ in range(tc):
    n, e = map(int, input().split())
    [*cave] = map(int, input().split())
    cave = [0] + cave
    connect = defaultdict(list)
    for _ in range(e):
        a, b, c = map(int, input().split())
        connect[a].append([b, c])

    # 해당 동굴의 최대값을 구함
    dp_cache = [0] * (n + 1)
    dp_path_cache = [0] * (n + 1)

    ans = dfs(1)
    path = [1]
    while dp_path_cache[path[-1]]:
        path.append(dp_path_cache[path[-1]])

    print(f"{ans} {len(path)}")
    print(*path)
