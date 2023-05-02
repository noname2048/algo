# timeout을 고쳐보자
import sys
from collections import defaultdict

sys.stdin = open("p1.txt", "r")
input = sys.stdin.readline

def main():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    a, b, c = map(int, input().split())

    def find_leaf():
        leaf = []
        for node in tree:
            if len(tree[node]) == 1:
                leaf.append(node)
        return leaf

    def bfs(start: int):
        cache = [-1] * ( n + 1)
        queue = [(start, 0)] # (node, dist)
        while queue:
            node, dist = queue.pop()
            if cache[node] != -1:
                continue
            cache[node] = dist
            for child in tree[node]:
                if cache[child] == -1:
                    queue.append((child, dist + 1))
        return cache

    leaf = find_leaf()
    cache_a = bfs(a)
    cache_b = bfs(b)
    cache_c = bfs(c)

    if a in leaf:
        print("YES")
        return

    for node in leaf:
        if cache_a[node] < cache_b[node] and cache_a[node] < cache_c[node]:
            print("YES")
            return

    print("NO")
    return

main()
