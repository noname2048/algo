import sys

sys.setrecursionlimit(1000000)

# debug = True
# if debug:
#     import logging

#     logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)
#     sys.stdin = open("input1.txt", "r")

input = sys.stdin.readline

dp_cache = [0, 0]
dp_path_cache = [0, 0]
dp_visited = {}
connect = [0, 0]
cave = [0, 0]


def dfs(idx):
    if dp_cache[idx]:
        # logging.debug(f"-- dfs({idx}) = {dp_cache[idx]}")
        return dp_cache[idx]

    if idx in dp_visited:
        return cave[idx]

    dp_visited[idx] = 1
    # logging.debug(f"open dfs({idx}) = {dp_cache[idx]}")
    value = 0
    next = 0
    for b, c in connect[idx]:
        cost_b = dfs(b) - c
        if cost_b >= value:
            value = cost_b
            next = b

    dp_path_cache[idx] = next
    dp_cache[idx] = value + cave[idx]
    # logging.debug(f"close dfs({idx}) = {dp_cache[idx]}")
    return dp_cache[idx]


ans_path = []
visited = {}


def visit(idx):
    if idx == 0:
        return
    if idx not in visited:
        ans_path.append(idx)
        visited[idx] = 1
        next = dp_path_cache[idx]
        visit(next)


tc = int(input())  # test_case
for _ in range(tc):
    n, e = map(int, input().split())
    [*cave] = map(int, input().split())
    cave = [0] + cave
    connect = [[] for _ in range(e + 2)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        connect[a].append([b, c])

    # 해당 동굴의 최대값을 구함
    dp_cache = [0] * (n + 1)
    dp_path_cache = [0] * (n + 1)
    dp_visited = {}
    ans_path = []
    visited = {}

    ans = dfs(1)
    visit(1)
    print(f"{ans} {len(ans_path)}")
    if len(ans_path) > 1:
        print(" ".join(map(str, ans_path)))
    else:
        print(ans_path[0])
