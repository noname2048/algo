# 무한루프 스터디
# 8.13(토), 8.16(화), 8.18(목)
# q3: 좌표 2배하기
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):

    dir_y = [1, 0, -1, 0]
    dir_x = [0, 1, 0, -1]

    K = 52 * 2
    board = [[0] * K for _ in range(K)]
    outline_board = [[0] * K for _ in range(K)]
    visited = [[0] * K for _ in range(K)]

    ldy, ldx = 1000, 1000
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for x in range(x1 * 2, x2 * 2 + 1):
            board[y1 * 2][x] = 1
            board[y2 * 2][x] = 1
        for y in range(y1 * 2, y2 * 2 + 1):
            board[y][x1 * 2] = 1
            board[y][x2 * 2] = 1

        if y1 < ldy or (y1 == ldy and x1 < ldx):
            ldy, ldx = y1, x1

    ldy *= 2
    ldx *= 2

    # outline
    q = deque()
    q.append([ldy, ldx, 0])
    outline_board[ldy][ldx] = 1

    while q:
        y, x, dir = q.popleft()
        for i in [-1, 0, 1, 2]:
            n_dir = (dir + i) % 4
            ny = y + dir_y[n_dir]
            nx = x + dir_x[n_dir]
            if board[ny][nx] == 1 and outline_board[ny][nx] == 0:
                outline_board[ny][nx] = 1
                q.append([ny, nx, dir + i])
                break

    # bfs
    q.clear()
    q.append([characterY * 2, characterX * 2, 0])
    while q:
        y, x, d = q.popleft()
        visited[y][x] = 1
        if y == itemY * 2 and x == itemX * 2:
            return d // 2

        for i in range(4):
            ny = y + dir_y[i]
            nx = x + dir_x[i]
            if outline_board[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append([ny, nx, d + 1])


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


test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
test_7()
