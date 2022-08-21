from sys import stdin
from collections import deque


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
    board = [[0] * (n + 1) for _ in range(n + 1)]
    filled_board = [[0] * (n + 1) for _ in range(n + 1)]
    count = 0

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
                    and 0 <= nx < n
                    and board[ny][nx] == item
                    and (dy, dx) not in connected_pos
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
                board[y][x] = 0
            return False

    def apply_gravity():
        nonlocal board
        for x in range(n):
            q = deque()
            for y in range(n):
                if board[y][x]:
                    q.append(board[y][x])
                    board[y][x] = 0
            for i in range(len(q)):
                board[i][x] = q[i]

    loop_count = 1
    while loop_count:
        once = False
        for y in range(n):
            for x in range(n):
                once = find_connected_and_fill_zero(y, x) or once

        if once == False:
            for y in range(n):
                print("".join(map(str, board[n])))
            return board

        apply_gravity()

        loop_count += 1
        if loop_count >= 99999:
            break

    print("somthing wrong")


solve()
