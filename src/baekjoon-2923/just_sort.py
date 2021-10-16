import sys

sys.stdin = open("input1.txt")

n = int(input())
a_list = []
b_list = []

for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

    a_list.sort()
    b_list.sort()
    b_list.reverse()

    g_max = 0
    for j in range(i + 1):
        g_max = max(a_list[j] + b_list[j], g_max)
    print(g_max)
