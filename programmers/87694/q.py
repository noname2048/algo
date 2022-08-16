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


x_tree = [[] for _ in range(51)]
y_tree = [[] for _ in range(51)]

arrival_x = -1
arrival_y = -1


def move(here_x, here_y, prev_dir, dir_policy):
    global x_tree, y_tree, arrival_x, arrival_y

    if here_x == arrival_x and here_y == arrival_y:
        return 0

    # 교차점이 있을때 마다, 방향을 바꿔야 한다
    # 정해진 방향으로
    next_dir = (prev_dir + dir_policy + 4) % 4

    move_dir = prev_dir
    if next_dir % 2 == 0:
        for y_edge in y_tree[here_x]:
            s, e, d = y_edge
            if s <= here_y <= e:
                move_dir = (d + dir_policy + 4) % 4
    else:
        for x_edge in x_tree[here_y]:
            s, e, d = x_edge
            if s <= here_x <= e:
                move_dir = (d + dir_policy + 4) % 4

    next_x = here_x + dir_x[move_dir]
    next_y = here_y + dir_y[move_dir]

    ret = move(next_x, next_y, move_dir, dir_policy) + 1
    return ret


def solution(rectangle, characterX, characterY, itemX, itemY):
    global x_tree, y_tree, arrival_x, arrival_y
    arrival_x = itemX
    arrival_y = itemY

    # save infomations
    y_tree = [[] for _ in range(51)]
    x_tree = [[] for _ in range(51)]

    for i, rect in enumerate(rectangle):
        lx, ly, rx, ry = rect

        y_tree[lx].append([ly, ry, D.LEFT])
        y_tree[rx].append([ly, ry, D.RIGHT])
        x_tree[ly].append([lx, rx, D.DOWN])
        x_tree[ry].append([lx, rx, D.UP])

    # 후보군 2개 구하기
    dir_candidate = []
    dir_cw_start = -1
    dir_ccw_start = -1

    for y_edge in y_tree[characterX]:
        s, e, d = y_edge
        if s <= characterY <= e:
            dir_candidate.append(d)

    for x_edge in x_tree[characterY]:
        s, e, d = x_edge
        if s <= characterX <= e:
            dir_candidate.append(d)

    if len(dir_candidate) == 2:
        a, b = dir_candidate
        if (a + 1) % 4 == b:
            dir_cw_start = (b + CW.CW + 4) % 4
            dir_ccw_start = (a + CW.CCW + 4) % 4
        else:
            dir_cw_start = (a + CW.CW + 4) % 4
            dir_ccw_start = (b + CW.CCW + 4) % 4
    else:
        dir_cw_start = (dir_candidate[0] + CW.CW + 4) % 4
        dir_ccw_start = (dir_candidate[0] + CW.CCW + 4) % 4

    cw_distance = 1 + move(
        characterX + dir_x[dir_cw_start],
        characterY + dir_y[dir_cw_start],
        dir_cw_start,
        CW.CW,
    )
    ccw_distance = 1 + move(
        characterX + dir_x[dir_ccw_start],
        characterY + dir_y[dir_ccw_start],
        dir_ccw_start,
        CW.CCW,
    )

    ret = min(cw_distance, ccw_distance)
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

"""
두개의 변이 만나는 곳에서 시작할때 문제가 있음
이 방식은 기억자의 외부에 있는 경우, 기억자인데 내부에서 시작하는 경우를 처리할 수 없음
"""
