n = int(input())
a_list = [0] * n
b_list = [0] * n

for i in range(n):
    a_list[i], b_list[i] = map(int, input().split())

    a_list.sort()
    b_list.sort()
    b_list.reverse()

    g_max = 0
    for i in range(n):
        g_max = max(a_list[i] + b_list[i], g_max)
        print(g_max)
