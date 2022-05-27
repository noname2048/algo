# 양궁대회
# 2022 카카오 블라인드 채용 level2
import functools


def re(remains, index, info):

    if index > 10:
        return 0, []

    shoot, not_shoot = 0, 0

    # shoot
    need_to_win = info[index] + 1
    if remains >= need_to_win:
        temp, shoot_state = re(remains - need_to_win, index + 1, info)
        shoot = temp + (10 - index)

    # not shoot
    temp, not_shoot_state = re(remains, index + 1, info)
    if info[index] == 0:
        not_shoot = temp + 0
    else:
        not_shoot = temp - (10 - index)

    if shoot > not_shoot:
        state = [need_to_win] + shoot_state
        return shoot, state
    else:
        state = [0] + not_shoot_state
        return not_shoot, state


def solution(n, info):
    score, state = re(n, 0, info)
    return state


def test_1():
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    ans = [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]

    answer = solution(n, info)
    assert ans == answer
