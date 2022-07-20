"""
Problem solving number 1
"""
from sys import stdin

input = stdin.readline

# n[1,50]
# m[n-1, 1000]


def solve(n, m, adj):
    n, m = map(int, input().split())
    adj = []
    for i in range(n):
        tmp = list(map(int, input.strip().split()))
        adj.append(tmp)

        for j in range(i + 1, n):
            if tmp[j] == "Y":
                loads.append((i, j))
    loads = []


if __name__ == "__main__":
    solve()
