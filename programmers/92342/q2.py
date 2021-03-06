from datetime import datetime

f = open("logs.txt", "w+")
t_str = datetime.now().strftime("%H:%M - logs")
print(t_str, file=f)


class Problem:
    def __init__(self, n, info):
        self.n = n
        self.info = info
        self.mx = -56
        self.mx_state = [0] * 11

    def re(self, remains, idx, state, score):
        if remains == 0:
            if self.mx < score:
                self.mx = score
                self.mx_state = state.copy()
            return

        if idx > 10:
            if self.mx < score:
                self.mx = score
                self.mx_state = state.copy()
            return

        # win
        w = self.info[idx] + 1
        if remains >= w:
            state[idx] = w
            self.re(remains - w, idx + 1, state, score + (10 - idx))
            state[idx] = 0
        # lose
        if self.info[idx] > 0:
            self.re(remains, idx + 1, state, score - (10 - idx))
        else:
            self.re(remains, idx + 1, state, score)


def solution(n, info):
    problem = Problem(n, info)
    state = [0] * 11
    problem.re(n, 0, state, 0)
    return problem.mx_state


def test_1():
    n = 2
    info = [0] * 11
    info[0], info[1] = 1, 1
    print(solution(n, info))


def test_2():
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    ans = [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
    print(solution(n, info))


# test_1()
test_2()
