# my1 을 정답이 되도록 수정 근데 어디가 틀렸던 건지 모르겠음 -> my4로 연결
POS = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]
ROW, COL, CNT = 0, 0, 0


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


# execute when 'a' turn
def recursion_a(board, aloc, bloc):
    global ROW, COL, CNT

    if board[aloc[0]][aloc[1]] == 0:  # lose_by_falling
        return -1

    can_move = []
    for i in range(4):
        ny, nx = aloc[0] + POS[i][0], aloc[1] + POS[i][1]
        if is_inboard([ny, nx]) and board[ny][nx] == 1:
            can_move += [i]

    if len(can_move) == 0:
        return -1  # lose_by_cannot_move_anymore

    win = []
    lose = []
    for j in can_move:
        y, x = aloc
        new_aloc = aloc[0] + POS[j][0], aloc[1] + POS[j][1]

        board[y][x] = 0
        temp = -recursion_b(board, new_aloc, bloc)
        board[y][x] = 1

        if temp > 0:
            win += [temp]
        else:
            lose += [temp]

    if win:
        return min(win) + 1
    return min(lose) - 1


# execute when 'b' turn
def recursion_b(board, aloc, bloc):
    global ROW, COL, CNT

    if board[bloc[0]][bloc[1]] == 0:  # lose_by_falling
        return -1

    can_move = []
    for a in range(4):
        ny, nx = bloc[0] + POS[a][0], bloc[1] + POS[a][1]
        if is_inboard([ny, nx]) and board[ny][nx] == 1:
            can_move += [a]

    if len(can_move) == 0:
        return -1  # lose_by_cannot_move_anymore

    win = []
    lose = []
    for k in can_move:
        y, x = bloc
        new_bloc = bloc[0] + POS[k][0], bloc[1] + POS[k][1]

        board[y][x] = 0
        temp = -recursion_a(board, aloc, new_bloc)
        board[y][x] = 1

        if temp > 0:
            win += [temp]
        else:
            lose += [temp]

    if win:
        return min(win) + 1
    return min(lose) - 1


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
