"""
무한루프 아침스터 8월 16일자 과제
주말 8월 13일 Jun의 집에서
"""
from enum import IntEnum
from re import L


class D(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class CW(IntEnum):
    CW = 1
    CCW = -1


dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

board = [[0] * 51 for _ in range(51)]
outline_board = [[0] * 51 for _ in range(51)]
visited = [[0] * 51 for _ in range(51)]


def mark_outline(here_x, here_y, prev_dir, stop_x, stop_y):
    global board, outline_board, visited
    start = True
    while (here_x != stop_x or here_y != stop_y) or start == True:
        start = False
        # mark
        outline_board[here_y][here_x] = 1
        # find cand
        for dir_change in range(-1, 2):
            next_dir = (prev_dir + dir_change) % 4
            next_x, next_y = here_x + dir_x[next_dir], here_y + dir_y[next_dir]

            if board[next_y][next_x] == 1:
                here_x = next_x
                here_y = next_y
                prev_dir = next_dir
                break
        else:
            # cannot find cand
            break


def bfs(here_x, here_y, stop_x, stop_y):
    global board, outline_board, visited

    q = []
    q.append([here_x, here_y, 0])
    visited[here_y][here_x] = 1

    while q:
        for i in range(0):
            


    if here_x == stop_x and here_y == stop_y:
        return 0

    visited[here_y][here_x] = 1

    ret = []
    for next_dir in range(4):
        next_x = here_x + dir_x[next_dir]
        next_y = here_y + dir_y[next_dir]

        if outline_board[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
            ret.append(1 + bfs(next_x, next_y, stop_x, stop_y))

    return min(ret)


def solution(rectangle, characterX, characterY, itemX, itemY):
    global board, outline_board, visited

    board = [[0] * 50 for _ in range(51)]
    outline_board = [[0] * 50 for _ in range(51)]
    visited = [[0] * 50 for _ in range(51)]

    ld_x, ld_y = 51, 51

    for x1, y1, x2, y2 in rectangle:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                board[y][x] = 1

        if y1 < ld_y:
            ld_y, ld_x = y1, x1
        elif y1 == ld_y and x1 < ld_x:
            ld_x = x1

    mark_outline(ld_x, ld_y, D.UP, ld_x, ld_y)
    ret = bfs(characterX, characterY, itemX, itemY)

    return ret


def test_1():
    rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, 17)


def test_2():
    rectangle = [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]]
    characterX = 9
    characterY = 7
    itemX = 6
    itemY = 1

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, 11)


def test_3():
    rectangle = [[1, 1, 5, 7]]
    characterX = 1
    characterY = 1
    itemX = 4
    itemY = 7

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, 9)


def test_4():
    rectangle = [[2, 1, 7, 5], [6, 4, 10, 10]]
    characterX = 3
    characterY = 1
    itemX = 7
    itemY = 10

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, 15)


def test_5():
    rectangle = [[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]]
    characterX = 1
    characterY = 4
    itemX = 6
    itemY = 3

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, 10)


def test_6():
    rectangle = [[1, 1, 4, 4], [2, 2, 5, 5], [3, 3, 7, 8]]
    characterX = 1
    characterY = 1
    itemX = 5
    itemY = 3

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, 6)


def test_7():
    rectangle, characterX, characterY, itemX, itemY, a = (
        [[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]],
        3,
        2,
        5,
        4,
        8,
    )

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(ans, a)


# test_1()
# test_2()
# test_3()
# test_4()
# test_5()
# test_6()
test_7()
