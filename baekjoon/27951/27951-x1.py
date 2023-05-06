# https://www.acmicpc.net/source/58143711
# 위의 코드를 참고
# 굉장하다
# 효율적이다.
# 1. main -solve - exit 으로 이어지는 코드
# 2. dict로 풀어냈다는것
# 3. dict 에 값이 없을경우 할당, 있을 경우 min 비교를 한 줄로 해결
# 4. sort 를 사용하여 중복을 제거한 점 (굳)

import sys

sys.stdin = open("p3.txt", "r")
input = lambda: sys.stdin.readline().strip()
dist = lambda u, v: min(abs(u - v), 10 - abs(u - v))

def main():
    n = int(input())
    t_arr = list(map(int, input().split()))

    print(solve(n, t_arr))

def solve(n, t_arr):
    states = {(0, 0, 0): 0}
    for t in t_arr:
        new_states ={}
        for (a, b, c), v in states.items():
            # a -> t
            va = v + dist(a, t)
            (na, nb, nc) = sorted((t, b, c))
            new_states[(na, nb, nc)] = min(new_states.get((na, nb, nc), va), va)

            # b- > t
            vb = v + dist(b, t)
            (na, nb, nc) = sorted((a, t, c))
            new_states[(na, nb, nc)] = min(new_states.get((na, nb, nc), vb), vb)


            # c -> t
            vc = v + dist(c, t)
            (na, nb, nc) = sorted((a, b, t))
            new_states[(na, nb, nc)] = min(new_states.get((na, nb, nc), vc), vc)

        states = new_states

    return min(states.values())

sys.exit(main())
