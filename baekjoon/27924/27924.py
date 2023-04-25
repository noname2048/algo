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
