import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # vertex, edges
    n, e = map(int, input().split())
    # vertex
    [*vertex] = map(int, [0] + input().split())
    # edge weight
    edge = [0] * (e + 1)
    for i in range(1, e + 1):
        a, b, c = map(int, input().split())
        edge[a].append((b, c))
        edge[b].append((a, c))

    dp_cache = [math.inf] * (n + 1)
    # bfs tree 로 접근
    path = []
    queue = [1]
    while queue:
        here = queue.pop()
        for next, cost in edge[here]:
            vertex[next] - cost

def bfs(here, cost, path):
    if dp_cache[here] == math.inf or dp_cache[here] > cost:
        dp_cache[here] = cost
        for next, develope_cost in edge[here]:
            bfs(next, cost + vertex[next] - develope_cost, path)
            
    return dp_cache[here]







     
