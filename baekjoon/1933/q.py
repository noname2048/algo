from typing import Callable
from sys import stdin


def preload() -> Callable[[], str]:
    data = """8
    1 11 5
    2 6 7
    3 13 9
    12 7 16
    14 3 25
    19 18 22
    23 13 29
    24 4 28
    """

    def make_generator():
        yield from map(str.strip, data.splitlines())

    my_generator = make_generator()

    def my_iterator():
        return next(my_generator)

    return my_iterator


input = stdin.readline
input = preload()


def solve():
    tc = int(input())
    cache = []
    for _ in range(tc):
        left, height, right = map(int, input().split())
        cache.append((left, height, "up"))
        cache.append((right, height, "down"))

    cache.sort()
    box = [0]
    mx = 0
    ans = []
    for item in cache:
        if item[-1] == "up":
            box.append(item[1])
        else:
            box.remove(item[1])

        if max(box) != mx:
            mx = max(box)
            ans.append([item[0], mx])

    print(" ".join([f"{a} {b}" for a, b in ans]))


if __name__ == "__main__":
    ans = solve()
