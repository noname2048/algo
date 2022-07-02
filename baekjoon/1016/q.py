from sys import stdin

input = stdin.readline


def solve():
    mn, mx = list(map(int, input().split()))
    doubles = []
    num, double = 2, 4
    while double < mx:
        doubles.append(double)
        num += 1
        double = num**2

    cnt = 0
    for num in range(mn, mx + 1):
        is_double_num = False
        for double in doubles:
            if num % double == 0:
                is_double_num = True
                break
            if num < double:
                break
        if not is_double_num:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    solve()
