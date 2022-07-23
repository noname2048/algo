from sys import stdin

input = stdin.readline


def solve():
    tc = int(input())
    for _ in range(tc):
        left, high, right = map(int, input().split())


if __name__ == "__main__":
    solve()
