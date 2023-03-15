from dataclasses import dataclass

@dataclass
class Q1:
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]

def solve():
    p = Q1
    solution(p.queue1, p.queue2)

def solution(queue1, queue2):
    answer = -2
    return answer


def inner_solution(q1, q2):
    q3 = q1 + q2
    l1, l2, l3 = len(q1), len(q2), len(q3)

    sum = sum(q3)
    if sum % 2 != 0:
        return -1

    ans = -1

    for_debug = []
    def update_ans(num: int) -> None:
        for_debug.append(num)
        if ans == -1 or num < ans:
            ans = num

    # i 포함, j 미포함, s 합
    i, j, s, half = 0, 0, 0, sum / 2
    while i < l3:
        if s < half and j <= l3:
            s += q3[j]
            j += 1
        elif s > half and i < l3:
            s -= q3[i]
            i += 1
        elif s == half:
            if j < l1:
                update_ans(j + l2 + i)
            if j == l1:
                update_ans(i)
            if j < l2:
                if i < l1:
                    update_ans(i + j - l1)
                elif i >= l1:
                    update_ans((j - l1) + l1 + (i - l1))
            if j == l2:
                if i < l1:
                    update_ans(i + l2)
                elif i >= l1:
                    update_ans(i - l1)
            #
            s -= q3[i]
            i += 1
        else:
            break

