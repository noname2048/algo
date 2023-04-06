# 손진영 유저로 부터 초기 상태부터 문제를 다 풀 수 있는 경우 확인

def solution(alp, cop, problems):
    # dp[i][j]: 알고력=i, 코딩력=j 상태에 도달하는 필요한 최단 시간
    # 0 <= i, j <= 150
    # 1 <= cost <= 100 이므로 dp[*][*] <= (150 + 150) * 100
    DP_MAX = 90_000
    I_MAX = 181
    dp = [[90_000]* I_MAX for _ in range(I_MAX)]

    # goal
    goal_alp = 0
    goal_cop = 0
    for problem in problems:
        goal_alp = max(goal_alp, problem[0])
        goal_cop = max(goal_cop, problem[1])

    if goal_alp <= alp and goal_cop <= cop:
        return 0

    # problem
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    for i in range(0, alp + 1):
        for j in range(0, cop + 1):
            dp[i][j] = 0

    dp[alp][cop] = 0
    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            for req_alp, req_cop, rw_alp, rw_cop, cost in problems:
                if i < req_alp or j < req_cop:
                    continue
                ni = i + rw_alp
                nj = j + rw_cop

                dp[ni][nj] = min(dp[i][j] + cost, dp[ni][nj])

    answer =  DP_MAX
    for i in range(goal_alp, I_MAX):
        for j in range(goal_cop, I_MAX):
            answer = min(dp[i][j], answer)

    return answer

Q1 = {
    "alp": 10,
    "cop": 10,
    "problems": [
        [10, 15, 2, 1, 2],
        [20, 20, 3, 3, 4],
    ],
}

Q2 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [0, 0, 2, 1, 2],
        [4, 5, 3, 1, 2],
        [4, 11, 4, 0, 2],
        [10, 4, 0, 4, 2],
    ],
}

Q3 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [0, 0, 1, 1, 1],
        [150, 150, 1, 1, 150],
    ],
}

Q4 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [4, 3, 1, 1, 150],
        [0, 0, 2, 2, 1],
    ],
}

Q5 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [0, 2, 1, 1, 150],
    ],
}

print(solution(**Q1))
print(solution(**Q2))
print(solution(**Q3))
print(solution(**Q4))
print(solution(**Q5))
