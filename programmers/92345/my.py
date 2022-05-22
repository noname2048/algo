# 사라지는 발판
# 2022 블라인드 카카오 문제
# 아침스터디
from copy import deepcopy
from enum import Enum


POS = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]


def move(idx, target):
    newpos = [0, 0]
    newpos[0], newpos[1] = target[0], target[1]
    newpos[0] += POS[idx][0]
    newpos[1] += POS[idx][1]
    return newpos


ROW, COL = 0, 0


def solution(board, aloc, bloc):
    global ROW, COL
    ROW = len(board)
    COL = len(board[0])

    answer = recursion_a(board, aloc, bloc)
    answer = abs(answer) - 1
    answer = int(answer)
    return answer


def is_inboard(loc):
    if 0 <= loc[0] < ROW and 0 <= loc[1] < COL:
        return True
    return False


def is_one(board, loc):
    y, x = loc
    return board[y][x] == 1


def is_zero(board, loc):
    return not is_one


def is_same(aloc, bloc):
    if aloc[0] == bloc[0] and aloc[1] == bloc[1]:
        return True
    return False


def debug_board_state(board, aloc, bloc):
    human_readable_board = deepcopy(board)
    human_readable_board[aloc[0]][aloc[1]] = "A"
    human_readable_board[bloc[0]][bloc[1]] = "B"
    return human_readable_board


# execute when 'a' turn
def recursion_a(board, aloc, bloc):
    global ROW, COL
    debug = debug_board_state(board, aloc, bloc)

    if is_zero(board, aloc):  # lose_by_falling
        return -1

    can_move = []
    for i in range(4):
        new_aloc = move(i, aloc)
        if is_inboard(new_aloc) and is_one(board, new_aloc):
            can_move += [i]

    if len(can_move) == 0:
        return -1  # lose_by_cannot_move_anymore

    win = {"mn": 1000, "path": -1}
    lose = {"mx": 0, "path": -1}
    for j in can_move:
        y, x = aloc
        new_aloc = move(j, aloc)

        board[y][x] = 0
        temp = -recursion_b(board, new_aloc, bloc)
        board[y][x] = 1

        if temp > 0:
            if win["mn"] > temp:
                win["mn"] = temp + 1
                win["path"] = j
        else:
            if lose["mx"] > temp:
                lose["mx"] = temp - 1
                lose["path"] = j

    if win["mn"] != 1000:
        result, path = win["mn"], win["path"]
    else:
        result, path = lose["mx"], lose["path"]

    print("A", aloc, f"r{result}", f"p{path}")
    return result


# execute when 'b' turn
def recursion_b(board, aloc, bloc):
    global ROW, COL
    debug = debug_board_state(board, aloc, bloc)

    if is_zero(board, bloc):  # lose_by_falling
        return -1

    can_move = []
    for i in range(4):
        new_bloc = move(i, bloc)
        if is_inboard(new_bloc) and is_one(board, new_bloc):
            can_move += [i]

    if len(can_move) == 0:
        return -1  # lose_by_cannot_move_anymore

    win = {"mn": 1000, "path": -1}
    lose = {"mx": 0, "path": -1}
    for j in can_move:
        y, x = bloc
        new_bloc = move(j, bloc)

        board[y][x] = 0
        temp = -recursion_a(board, aloc, new_bloc)
        board[y][x] = 1

        if temp > 0:
            if win["mn"] > temp:
                win["mn"] = temp + 1
                win["path"] = j
        else:
            if lose["mx"] > temp:
                lose["mx"] = temp - 1
                lose["path"] = j

    if win["mn"] != 1000:
        result, path = win["mn"], win["path"]
    else:
        result, path = lose["mx"], lose["path"]

    print("B", bloc, f"r{result}", f"p{path}")
    return result


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
    test_1()
