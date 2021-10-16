import sys

sys.stdin = open("input1.txt")

n = int(input())
a_list = [0] * 101
b_list = [0] * 101

for i in range(n):
    a, b = map(int, input().split())
    a_list[a] += 1
    b_list[b] += 1

    g_max = 0
    j = 1
    j_cnt = 0
    k = 100
    k_cnt = 0
    for _ in range(i + 1):

        if j_cnt == a_list[j]:
            j_cnt = 0
            j += 1

        if not a_list[j]:
            while not a_list[j]:
                j += 1

        j_cnt += 1

        if k_cnt == b_list[k]:
            k_cnt = 0
            k -= 1

        if not b_list[k]:
            while not b_list[k]:
                k -= 1

        k_cnt += 1

        g_max = max(g_max, j + k)

    print(g_max)
