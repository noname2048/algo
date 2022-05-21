# 사라지는 발판
# 2022 블라인드 카카오 문제
# 아침스터디
from enum import Enum


POS = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]


def move(idx, target):
    newpos = target.copy()
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


# execute when 'a' turn
def recursion_a(board, aloc, bloc):
    global ROW, COL

    if is_zero(board, aloc):  # lose_by_falling
        return -1

    can_move = []
    for i in range(4):
        new_aloc = move(i, aloc)
        if is_inboard(new_aloc) and is_one(board, new_aloc):
            can_move += [i]

    if len(can_move) == 0:
        return -1  # lose_by_cannot_move_anymore

    cache = []
    for j in can_move:
        y, x = aloc
        new_aloc = move(j, aloc)
        board[y][x] = 0
        temp = -recursion_b(board, new_aloc, bloc)
        cache += [temp]
        board[y][x] = 1

    win_best, lose_best = 1000, 0
    for k in cache:
        if k > 0:
            win_best = min(k, win_best)
        else:
            win_best = min(k, lose_best)

    if win_best != 1000:
        return win_best + 1
    return lose_best - 1


# execute when 'b' turn
def recursion_b(board, aloc, bloc):
    global ROW, COL

    if is_zero(board, aloc):  # lose_by_falling
        return -1

    can_move = []
    for i in range(4):
        new_aloc = move(i, aloc)
        if is_inboard(new_aloc) and is_one(board, new_aloc):
            can_move += [i]

    if len(can_move) == 0:
        return -1  # lose_by_cannot_move_anymore

    cache = []
    for j in can_move:
        y, x = aloc
        new_bloc = move(j, bloc)
        board[y][x] = 0
        temp = -recursion_a(board, aloc, new_bloc)
        cache += [temp]
        board[y][x] = 1

    win_best, lose_best = 1000, 0
    for k in cache:
        if k > 0:
            win_best = min(k, win_best)
        else:
            win_best = min(k, lose_best)

    if win_best != 1000:
        return win_best + 1
    return lose_best - 1


if __name__ == "__main__":
    # q1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # a, b = [1, 0], [1, 2]
    # ans = solution(q1, a, b)

    q = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    a, b = [1, 0], [1, 2]
    ans = solution(q, a, b)

    # q = [[1, 1, 1, 1, 1]]
    # a, b = [0, 0], [0, 4]
    # ans = solution(q, a, b)

    print(ans)
