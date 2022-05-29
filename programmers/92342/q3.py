# Too many wrong codes, so not split file by file
# I try fix this code in here

from datetime import datetime

f = open("logs.txt", "w+")
t_str = datetime.now().strftime("%H:%M - logs")
print(t_str, file=f)


class Problem:
    def __init__(self, n, info):
        self.n = n
        self.info = info
        self.mx = 0
        self.mx_state = [0] * 11

    def re(self, remains, idx, state, score):
        if idx == 10:
            state[idx] = remains
            print(f"{remains:2d} {idx:2d} {state} {score:3d} {self.mx:2d}", file=f)
            if self.mx < score:
                self.mx = score
                self.mx_state = state.copy()
            elif self.mx == score:
                for i in range(10, -1, -1):
                    lo, gl = state[i], self.mx_state[i]
                    if lo > gl:
                        self.mx_state = state.copy()
                        break
                    elif lo < gl:
                        break

            state[idx] = 0
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

    if problem.mx <= 0:
        return [-1]
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


def test_3():
    n = 9
    info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
    ans = [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
    print(solution(n, info))


# test_1()
test_3()
