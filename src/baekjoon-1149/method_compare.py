import sys
import time

# 기존 메소드
t = 0
for i in range(100):
    sys.stdin = open("long_input.txt", "r")
    s = time.time()
    cost_list = []
    for house in range(int(input())):
        cost_list.append(list(map(int, input().split())))
    t += time.time() - s
print(t)

# 나중 메소드
t = 0
for i in range(100):
    sys.stdin = open("long_input.txt", "r")
    s = time.time()
    read = sys.stdin.readline

    n = int(read().strip())
    dp = [list(map(int, read().strip().split()))]
    for i in range(1, n):
        r, g, b = map(int, read().strip().split())
        dp.append([r, g, b])
    t += time.time() - s
print(t)
