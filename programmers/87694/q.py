"""
무한루프 아침스터 8월 16일자 과제
주말 8월 13일 Jun의 집에서
"""
from enum import Enum
from re import L


class D(Enum, int):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]


def solution(rectangle, characterX, characterY, itemX, itemY):
    # find most left down coner to start
    start_x, start_y, start_idx = 51, 51, -1

    for i, rect in enumerate(rectangle):
        lx, ly, rx, ry = rect
        if ly < start_y:
            start_x, start_y, start_idx = lx, ly, i

    # start to up

    answer = 0
    return answer
