from collections import defaultdict


N = int(input())
conn = defaultdict(dict)
for _ in range(N):
    x, y = map(int, input().split())
    conn[x][y] = True
    conn[y][x] = True

a, b, c = map(int, input().split())
