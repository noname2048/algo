from sys import stdin
from collections import deque


DEBUG = 1


def predata():
    def make_gen():
        s = """6 3
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
"""
        yield from s.splitlines()

    gen = make_gen()

    def make_iter_func():
        return next(gen)

    return make_iter_func


input = stdin.readline
input = predata()


def solve():
    n, k = map(int, input().split())
    board = [[0] * (10) for _ in range(n)]
    filled_board = [[0] * (10) for _ in range(n)]
    count = 0

    for y in range(n):
        tmp = input().strip()
        str_list = [*tmp]
        board[y] = list(map(int, str_list))

    def find_connected_and_fill_zero(y, x):
        nonlocal count, board, n, k
        if filled_board[y][x] or board[y][x] == 0:
            return

        item = board[y][x]
        count += 1
        connected_pos = {}
        q = deque()

        q.append((y, x))
        connected_pos[(y, x)] = 1

        while q:
            y, x = q.popleft()
            for dy, dx in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < n
                    and 0 <= nx < 10
                    and board[ny][nx] == item
                    and (ny, nx) not in connected_pos
                ):
                    connected_pos[(ny, nx)] = 1
                    q.append((ny, nx))

        if len(connected_pos) >= k:
            for y, x in connected_pos.keys():
                board[y][x] = 0
                filled_board[y][x] = count
            return True
        else:
            for y, x in connected_pos.keys():
                filled_board[y][x] = count
            return False

    def apply_gravity():
        nonlocal board, filled_board
        for x in range(10):
            q = deque()
            for y in range(n):
                filled_board[n - y - 1][x] = 0
                if board[n - y - 1][x]:
                    q.append(board[n - y - 1][x])
                    board[n - y - 1][x] = 0
            for i in range(len(q)):
                board[n - i - 1][x] = q[i]

    def apply_left_gravity():
        nonlocal board, filled_board, n
        new_board = [[0] * 10 for _ in range(n)]
        to, from_ = 0, 0
        for x in range(10 - 1):
            sum_ = 0
            for y in range(n):
                sum_ += board[y][x]

            if sum_ == 0:
                from_ += 1
            else:
                for y in range(n):
                    new_board[y][to] = board[y][from_]
                to += 1
                from_ += 1

        board = new_board

    if DEBUG:
        print("-" * 10 + str(0))
        for y in range(n):
            print("".join(map(str, board[y])))

    loop_count = 1
    while loop_count:
        once = False
        for y in range(n):
            for x in range(10):
                once = find_connected_and_fill_zero(y, x) or once

        if DEBUG:
            print("-" * 10 + str(loop_count))
            for y in range(n):
                print("".join(map(str, board[y])))

        if once == False:
            if not DEBUG:
                for y in range(n):
                    print("".join(map(str, board[y])))
            return board

        apply_gravity()
        # apply_left_gravity()

        loop_count += 1
        if loop_count >= 99999:
            break

    print("somthing wrong")


solve()
