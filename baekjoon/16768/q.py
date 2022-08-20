from sys import stdin

input = stdin.readline


def solve():
    n, k = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[0] * (n + 1) for _ in range(n + 1)]
