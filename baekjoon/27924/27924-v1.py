from collections import defaultdict
import sys

sys.stdin = open("p1.txt", "r")

BIG = 900_000
N = int(input())
connection = defaultdict(dict)
for _ in range(N - 1):
    x, y = map(int, input().split())
    connection[x][y] = True
    connection[y][x] = True

a, b, c = map(int, input().split())
# 어떻게 해야하지
# abc를 일직선상에 놓고, 생각하면 편할지도
# 어디 위치에 있을지 모르는 abc를 어떻게 일직선상에 놓을 수 있을까
# 일직선상에 못놓을 수 있음
# a, b를 먼저 일직선상에,
# b, c를 일직선상에 놓는다.
# 문제를 간략하게 해서 a, b 만 생각한다.
# a, b를 일직선상에 놓는다.

## 2
# a 를 기준으로 bfs, b 를 기준으로 bfs
# c 를 기준으로 bfs 를 펼처 거리를 기록한다.
# 리프노드까지 a < b, c 면 탈출 성공

def bfs(N, BIG, start, tree):
    """start -> bfs recode with cache
    
    example: bfs(0, mem)
    """
    cache = [BIG] * (N + 1)
    queue = [(start, 0)] # pair(node, dist)
    
    while queue:
        here, dist = queue.pop()
        cache[here] = dist
        for next in tree[here].keys():
            if cache[next] == BIG and next not in queue:
                queue.append((next, (dist + 1)))

    return cache

def search_leaf_node(N, tree):
    answer = []
    for k, v in tree.items():
        if len(v) == 1:    
            answer.append(k)

    return answer

leaf_node = search_leaf_node(N, connection)
a_cache = bfs(N, BIG, a, connection)
b_cache = bfs(N, BIG, b, connection)
c_cache = bfs(N, BIG, c, connection)

if a in leaf_node:
    print("YES")
else:
    success = False
    for i in leaf_node:
        if a_cache[i] < b_cache[i] and a_cache[i] < c_cache[i]:
            success = True

    if success:
        print("YES")
    else:
        print("NO")
