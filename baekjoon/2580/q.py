from sys import stdin

input = stdin.readline


def predata():
    s = """ 0 3 5 4 6 9 2 7 8
            7 8 2 1 0 5 6 0 9
            0 6 0 2 7 8 1 3 5
            3 2 1 0 4 6 8 9 7
            8 0 4 9 1 3 5 0 6
            5 9 6 8 2 0 4 1 3
            9 1 7 6 5 2 0 8 0
            6 0 3 7 0 1 9 5 2
            2 5 8 3 9 4 7 6 0"""

    s = """ 0 0 0 0 0 0 0 0 0
            7 8 2 1 3 5 6 4 9
            4 6 9 2 7 8 1 3 5
            3 2 1 5 4 6 8 9 7
            0 0 0 0 0 0 0 0 0
            5 9 6 8 2 7 4 1 3
            9 1 7 6 5 2 3 8 4
            6 4 3 7 8 1 9 5 2
            0 0 0 0 0 0 0 0 0"""

    s = """0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0"""

    def make_gen():
        yield from s.splitlines()

    closer = make_gen()

    def make_iter():
        return next(closer)

    return make_iter


input = predata()


def test_ans(board):
    ans = """1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1"""

    ans_board = []
    for line in ans.splitlines():
        ans_board.append(list(map(int, line.strip().splite())))

    for y in range(9):
        for x in range(9):
            assert ans_board[y][x] == board[y][x]


def solve():
    board = []
    zero_points = []

    for y in range(9):
        board.append(list(map(int, input().strip().split())))
        for x in range(9):
            if board[y][x] == 0:
                zero_points.append((y, x))

    def get_candidate(y, x):
        parent = set(range(1, 10))

        for i in range(9):
            if board[y][i]:
                parent.discard(board[y][i])
            if board[i][x]:
                parent.discard(board[i][x])

        oy = y // 3
        ox = x // 3

        for dy in range(3):
            for dx in range(3):
                ty = oy * 3 + dy
                tx = ox * 3 + dx
                if board[ty][tx]:
                    parent.discard(board[ty][tx])

        return list(parent)

    find_ = False
    last_index = len(zero_points)

    def re(index):
        nonlocal zero_points, find_, board

        if index >= last_index:
            find_ = True
            return

        here_y, here_x = zero_points[index]
        candidates = get_candidate(here_y, here_x)
        for i in candidates:
            board[here_y][here_x] = i
            # print(f"index ({index}) [{here_y} {here_x}] = {candidates}")
            re(index + 1)
            if find_ == True:
                return

        board[y][x] = 0

    re(0)
    for i in range(9):
        print(" ".join(map(str, board[i])))


if __name__ == "__main__":
    solve()
