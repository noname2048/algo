import sys
import math

sys.stdin = open("input.txt", "r")


def solution(cost_list):
    n = len(cost_list)
    global_minima = math.inf
    stack = []

    for idx in range(3):
        last_house = 0
        last_choice = idx
        cost = cost_list[0][idx]

        stack.append(
            (
                last_house,
                last_choice,
                cost,
            )
        )

    while stack:
        house, choice, cost = stack.pop()

        if house >= n - 1:  # stack 의 끝에 다다른 경우
            global_minima = min(global_minima, cost)
            continue

        for idx in range(3):
            target_house = house + 1
            if choice != idx:  # 이전 선택결과와 달라야 선택
                new_cost = cost + cost_list[target_house][idx]
                if new_cost <= global_minima:  # 가지치기
                    stack.append((target_house, idx, new_cost))

    return global_minima


cost = []
desc = []

for house in range(int(input())):
    temp = list(map(int, input().split()))
    # desc_temp_idx = sorted(range(3), key=lambda k: -temp[k])
    cost.append(temp)
    # desc.append(desc_temp_idx)

print(solution(cost))
