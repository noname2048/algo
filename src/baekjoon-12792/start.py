def solution(table):
    l = len(table)
    for i in range(l):
        if (i + 1) == table[i]:
            return -1

    rotate = [ele for ele in table]
    for ans in range(2, 2 * 10 ** 9 + 1):
        rotate = [table[i - 1] for i in rotate]

        same_filter = [x for i, x in enumerate(rotate) if (i + 1) == x]
        if not same_filter:
            return ans

    return -1


n = input()
table = list(map(int, input().split()))
print(solution(table))
