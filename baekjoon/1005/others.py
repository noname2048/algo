import io, os, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def dp(i):
    if cum_d[i] < 0:
        cum_d[i] = 0
        for e in edges[i]:
            cum_d[i] = max(cum_d[i], dp(e))
        cum_d[i] += d[i]
    return cum_d[i]


def solve():
    global edges, d, cum_d
    n, k = map(int, input().split())
    d = tuple(map(int, input().split()))
    cum_d = [-1] * n
    edges = [set() for _ in range(n)]
    for _ in range(k):
        x, y = map(lambda x: int(x) - 1, input().split())
        edges[y].add(x)
    w = int(input()) - 1
    ans = dp(w)
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
