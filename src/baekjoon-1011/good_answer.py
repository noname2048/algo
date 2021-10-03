import sys

n = int(input())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x

    base = int(pow(distance - 1, 0.5))
    if distance <= base * (base + 1):
        print(base * 2)
    else:
        print(base * 2 + 1)
