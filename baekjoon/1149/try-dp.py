import sys

sys.stdin = open("input.txt", "r")
import math

dp = None
n = -1


def re(house, choice):
    global n
    global dp

    if dp[house][choice] != math.inf:
        return dp[house][choice]

    if house >= n - 1:
        return cost_list[house][choice]

    new_cost = cost_list[house][choice] + min(
        re(house + 1, (choice + 1) % 3), re(house + 1, (choice + 2) % 3)
    )

    return new_cost


def solution(cost_list):
    global n
    global dp

    n = len(cost_list)
    dp = [[math.inf] * 3 for _ in range(n)]

    global_min = math.inf
    for idx in range(3):
        temp = re(0, idx)
        global_min = min(global_min, temp)

    return global_min


cost_list = []
for house in range(int(input())):
    cost_list.append(list(map(int, input().split())))
print(solution(cost_list))
