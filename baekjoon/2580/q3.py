from sys import stdin


def pre_data():
    s = """ 0 0 0 0 0 0 0 0 0
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


input = pre_data()


# input = stdin.readline


board = []
zeros = []


def get_candidate(y, x):
    global board

    candidates = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    for i in range(9):
        hori = board[y][i]
        vert = board[i][x]
        if hori in candidates:
            candidates.pop(hori)
        if vert in candidates:
            candidates.pop(vert)

    if len(candidates) == 0:
        return []

    oy, ox = y // 3, x // 3
    for i in range(3):
        for j in range(3):
            tmp = board[oy * 3 + i][ox * 3 + j]
            if tmp in candidates:
                candidates.pop(tmp)

    return list(candidates.keys())


find_ = False


def re(index):
    global board, find_

    if index >= len(zeros):
        find_ = True
        return

    y, x = zeros[index]
    candidates = get_candidate(y, x)
    for i in candidates:
        board[y][x] = i
        re(index + 1)
        if find_:
            return

    board[y][x] = 0


def solve():
    global board
    for _ in range(9):
        board.append(list(map(int, input().split())))

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                zeros.append((y, x))

    re(0)
    for i in range(9):
        print(" ".join(map(str, board[i])))


if __name__ == "__main__":
    solve()
