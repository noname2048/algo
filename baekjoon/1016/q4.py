from sys import stdin

input = stdin.readline


def solve():
    mn, mx = map(int, input().split())
    numbers = set()

    square_root = int(mx**0.5)
    for num in range(2, square_root + 1):
        square_num = num**2
        q, r = divmod(mn, square_num)

        st = q if r == 0 else q + 1
        ed = mx // square_num

        for i in range(st, ed + 1):
            numbers.add(square_num * i)

    ans = mx - mn + 1 - len(numbers)
    print(ans)


if __name__ == "__main__":
    solve()
