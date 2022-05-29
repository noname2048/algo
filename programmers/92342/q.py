# 양궁대회
# 2022 카카오 블라인드 채용 level2
import functools
from datetime import datetime

f = open("logs.txt", "w+")
t_str = datetime.now().strftime("%H:%M - logs")
print(t_str, file=f)

mx = -999
mx_state = []


def re(remains, index, info, state):
    global mx, mx_state

    if index > 10:
        return 0

    shoot, not_shoot = 0, 0

    # shoot
    need_to_win = info[index] + 1
    if remains >= need_to_win:
        state[index] = need_to_win
        temp = re(remains - need_to_win, index + 1, info, state)
        state[index] = 0
        shoot = temp + (10 - index)

    # not shoot
    temp = re(remains, index + 1, info, state)
    if info[index] == 0:
        not_shoot = temp + 0
    else:
        not_shoot = temp - (10 - index)

    if shoot > not_shoot:
        print(f"shoot {index:2d}, {mx_state} {mx}", file=f)
        if mx < shoot:
            mx = shoot
            mx_state = state.copy()
        return shoot
    else:
        print(f" n ot {index:2d}, {mx_state} {mx}", file=f)
        if mx < not_shoot:
            mx = not_shoot
            mx_state = state.copy()
        return not_shoot


def solution(n, info):
    state = [0] * 11
    score = re(n, 0, info, state)
    return mx_state


def test_1():
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    ans = [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]

    answer = solution(n, info)
    assert ans == answer


test_1()
f.close()
