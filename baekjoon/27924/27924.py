from collections import defaultdict


N = int(input())
conn = defaultdict(dict)
for _ in range(N):
    x, y = map(int, input().split())
    conn[x][y] = True
    conn[y][x] = True

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

def bfs(start, tree):
    """start -> bfs recode with cache
    
    example: bfs(0, mem)
    """
    cache = [-1] * len(tree)
    queue = [(start, 0)]
    
    while queue:
        here, dist = queue.pop()
        cache[here] = dist
        for next in tree[here]:
            if cache == -1 and next not in queue:
                queue.append((next, (dist + 1)))
    return cache

a_c = bfs(a, tree)
b_c = bfs(b, tree)
c_c = bfs(c, tree)
