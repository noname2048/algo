import sys
import math
# log = open("log.txt", "w")
sys.stdin = open("input1.txt", "r")
input = sys.stdin.readline

global_max_cost = 0
global_cache_path = None

def dfs(here, cost, path):
    global global_max_cost
    global global_cache_path

    # log.write(f"{here}({cost}) - {path}\n")
    if dp_cache[here] == math.inf or dp_cache[here] < cost:
        dp_cache[here] = cost

        if global_max_cost < cost:
            global_max_cost = cost
            global_cache_path = path
            # log.write(f"star\n")     

        for next, develope_cost in edge[here]:
            path = path + [next]
            dfs(next, cost + vertex[next] - develope_cost, path)
            path.pop()
            
    return dp_cache[here]

t = int(input())
for _ in range(t):
    # vertex, edges
    n, e = map(int, input().split())
    # vertex
    [*vertex] = map(int, [0] + input().split())
    # edge weight (directional)
    edge = [[] for _ in range(e + 2)]
    for i in range(1, e + 1):
        a, b, c = map(int, input().split())
        edge[a].append((b, c)) # 예제 1 - 테스트 3번을 보면 분명한 방향성이 있다.

    dp_cache = [math.inf] * (n + 1)

    global_max_cost = 0
    global_cache_path = []
    value = dfs(1, vertex[1], [1])
    print(global_max_cost, len(global_cache_path))
    print(global_cache_path[0] if len(global_cache_path) == 1 else " ".join(map(str, global_cache_path)))
