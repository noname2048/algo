from sys import stdin

input = stdin.readline


def solve():
    mn, mx = map(int, input().split())

    numbers = set()

    num = 2
    square_num = num**2
    while square_num <= mx:

        q, r = divmod(square_num, mn)
        mi = square_num * q if r == 0 else square_num * (q + 1)

        while mi <= mx:
            numbers.add(mi)
            mi += square_num

        num += 1
        square_num = num**2

    ans = mx - mn + 1 - len(numbers)
    print(ans)


if __name__ == "__main__":
    solve()
