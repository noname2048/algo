from sys import stdin

input = stdin.readline


def predata():
    s = """0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0"""

    def make_gen():
        yield from s.splitlines()

    closer = make_gen()

    def make_iter():
        return next(closer)

    return make_iter


input = predata()


def solve():
    board = []

    for y in range(9):
        tmp = map(int, input().split())
        tmp = list(tmp)
        board.append(tmp)

    def get_candidate(y, x):
        parent = set(range(1, 10))

        for i in range(9):
            if board[y][i]:
                parent.discard(board[y][i])
            if board[i][x]:
                parent.discard(board[i][x])

        oy = y % 3
        ox = x % 3

        for dy in range(3):
            for dx in range(3):
                ty = oy + dy
                tx = ox + dx
                if board[ty][tx]:
                    parent.discard(board[ty][tx])

        return list(parent)

    find_ = False

    def re(yy, xx):
        if yy >= 9:
            return board

        while board[yy][xx] != 0:
            nx = xx + 1
            if nx >= 9:
                nx = 0
                ny = yy + 1
            else:
                ny = yy

            yy = ny
            xx = nx

        nx = xx + 1
        if nx >= 9:
            nx = 0
            ny = yy + 1
        else:
            ny = yy

        if board[yy][xx] == 0:
            cands = get_candidate(yy, xx)

            for i in cands:
                board[yy][xx] = i
                re(ny, nx)
                if find_:
                    return

    re(0, 0)
    print(board)


solve()
