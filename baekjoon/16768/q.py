from sys import stdin
from collections import deque


def predata():
    def make_gen():
        s = """90 6
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000200000
0000200000
0000300000
0000100000
0000100000
0000200000
0000202010
0200203030
3100202030
2300102120
1220132310
1130332120
3330232210
2230112323
2220322223
1110323221
2112221131
2111331233
3313322222
3323131331
2122132313
1321131333
3211213213
2333323213
3121123322
3112322113
1321123222
3122232121
2131332111
3323333211
3322211121
2121133323
1123333312
1233223311
2313113223
1313131312
2122122131
1312233111
1122123311
1313113133
2121333222
1333231131
2312112211
3332222122
2311212133
1311123133
1133231223
1311231323
1332313211
3231123123
1321211221
3333332232
2122113313
1211213221
1111122132
1111311231
1321113222
2333312331
1223331322
3132311212
1321313111
2232123122
3313332323
3223231121
2232131321
1222233223
3131222111
3133223113
2211112133
2233231313
3132313311
3312221221
2233122131
3323233131
2212113311
3222133323
1322332312
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

    # print("-" * 10 + str(0))
    # for y in range(n):
    #     print("".join(map(str, board[y])))

    loop_count = 1
    while loop_count:
        once = False
        for y in range(n):
            for x in range(10):
                once = find_connected_and_fill_zero(y, x) or once

        # print("-" * 10 + str(loop_count))
        # for y in range(n):
        #     print("".join(map(str, board[y])))

        if once == False:
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
