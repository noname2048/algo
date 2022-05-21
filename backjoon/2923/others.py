import sys  # turgon314 님 코드 참조

sys.stdin = open("input1.txt", "r")
input = sys.stdin.readline
n = int(input())
a_list, b_list = [0] * 101, [0] * 101
for _ in range(n):
    a, b = map(int, input().split())
    a_list[a] += 1
    b_list[b] += 1

    ans, i, j, x, y = 0, 1, 100, a_list[1], b_list[100]
    while j > 0:  # j DESC
        if y == 0:
            j -= 1
            y = b_list[j]
        elif y > x:
            i += 1
            y -= x
            x = a_list[i]
        elif y == x:
            ans = max(ans, i + j)
            i += 1
            j -= 1
            x, y = a_list[i], b_list[j]
        else:
            ans = max(ans, i + j)
            x -= y
            j -= 1
            y = b_list[j]
    print(ans)
