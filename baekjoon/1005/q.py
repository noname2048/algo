from sys import stdin, setrecursionlimit
from collections import defaultdict
from io import StringIO

setrecursionlimit(10001)
input = stdin.readline


def pre_data():
    from pathlib import Path

    dir = Path(__file__).parent
    with open(dir / "data2.txt", "r") as f:
        txt = f.readlines()

    def gen():
        nonlocal txt
        yield from txt

    single = gen()

    def ter():
        nonlocal single
        return next(single).strip()

    return ter


input = pre_data()


def solve():
    tc = int(input())
    n, k = 0, 0
    d = [0] * n
    graph = defaultdict(set)
    cache = [-1] * (n + 1)

    def recursion(idx):
        nonlocal cache, graph, d
        if cache[idx] > 0:
            return cache[idx]
        # no parents
        if not graph[idx]:
            cache[idx] = d[idx]
            print(f"idx{idx}: {cache[idx]}")
            return cache[idx]
        # have parents
        values = [recursion(parent) for parent in graph[idx]]
        cache[idx] = max(values) + d[idx]
        print(f"idx{idx}: {cache[idx]}")
        return cache[idx]

    for _ in range(tc):
        n, k = map(int, input().split())
        d = map(int, ("0 " + input()).split())
        d = list(d)
        cache = [-1] * (n + 1)
        graph = defaultdict(set)
        for _ in range(k):
            p, c = map(int, input().split())
            graph[c].add(p)
        w = int(input())
        ans = recursion(w)
        print(ans)


if __name__ == "__main__":
    solve()
