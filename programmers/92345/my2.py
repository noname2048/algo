from copy import deepcopy


UP = [-1, 0]
RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
DIR = [UP, RIGHT, DOWN, LEFT]

ROW, COL = 0, 0
CNT = 0


def is_zero(board, location):
    y, x = location
    return board[y][x] == 0


def re_a(board, aloc, bloc) -> int:
    global ROW, COL, CNT
    target = aloc
    if is_zero(board, target):  # stading on zero platform
        return 0

    candidates = []
    for dir in range(4):
        y, x = target
        ny, nx = target[0] + DIR[dir][0], target[1] + DIR[dir][1]
        if 0 <= ny < ROW and 0 <= nx < COL and board[ny][nx] == 1:
            board[y][x] = 0
            temp = re_b(board, [ny, nx], bloc) + 1
            board[y][x] = 1

            candidates += [[dir, temp]]

    if len(candidates) == 0:  # cannot move anymore
        return 0

    # win / lose / debug_path
    odd, even, path = 999, 0, -1

    for d, t in candidates:
        if t % 2 == 1:
            if odd > t:  # choose min odd
                odd, path = t, d
        else:
            if even < t:  # choose max even``
                even, path = t, d

    ## LOG
    # CNT += 1
    # state = deepcopy(board)
    # ay, ax = aloc
    # by, bx = bloc
    # state[ay][ax] = "A"
    # state[by][bx] = "B"
    # print("A", CNT)
    # print(state)
    # print(candidates)
    # print(odd, even, path)

    if odd != 999:
        return odd
    return even


def re_b(board, aloc, bloc) -> int:
    global ROW, COL, CNT
    target = bloc
    if is_zero(board, target):  # stading on zero platform
        return 0

    candidates = []
    for dir in range(4):
        y, x = target
        ny, nx = target[0] + DIR[dir][0], target[1] + DIR[dir][1]
        if 0 <= ny < ROW and 0 <= nx < COL and board[ny][nx] == 1:
            board[y][x] = 0
            temp = re_a(board, aloc, [ny, nx]) + 1
            board[y][x] = 1

            candidates += [[dir, temp]]

    if len(candidates) == 0:  # cannot move anymore
        return 0

    # win / lose / debug_path
    odd, even, path = 999, 0, -1

    for d, t in candidates:
        if t % 2 == 1:
            if odd > t:  # choose min odd
                odd, path = t, d
        else:
            if even < t:  # choose max even
                even, path = t, d

    ## LOG
    # CNT += 1
    # state = deepcopy(board)
    # ay, ax = aloc
    # by, bx = bloc
    # state[ay][ax] = "A"
    # state[by][bx] = "B"
    # print("B", CNT)
    # print(state)
    # print(candidates)
    # print(odd, even, path)

    if odd != 999:
        return odd
    return even


def solution(board, aloc, bloc):
    global ROW, COL
    ROW, COL = len(board), len(board[0])
    answer = re_a(board, aloc, bloc)
    return answer


def test_1():
    q = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    a, b = [1, 0], [1, 2]
    ans = solution(q, a, b)
    assert ans == 5


def test_2():
    q = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    a, b = [1, 0], [1, 2]
    ans = solution(q, a, b)
    assert ans == 4


def test_3():
    q = [[1, 1, 1, 1, 1]]
    a, b = [0, 0], [0, 4]
    ans = solution(q, a, b)
    assert ans == 4


def test_4():
    q = [[1]]
    a, b = [0, 0], [0, 0]
    ans = solution(q, a, b)
    assert ans == 0


def test_5():
    q = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
    a, b = [0, 0], [3, 3]
    ans = solution(q, a, b)
    assert ans == 8


if __name__ == "__main__":
    test_5()
