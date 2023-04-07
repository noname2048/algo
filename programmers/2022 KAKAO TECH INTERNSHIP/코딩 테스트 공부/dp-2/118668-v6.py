# v5로 부터 케이스 더 추가
# 카카오 해설에서 힌트를 얻어 진행
# 풀이 완료


def solution(alp, cop, problems):
    DP_MAX = 90_000
    REQ_MAX = 150
    dp = [[DP_MAX] * (REQ_MAX + 1) for _ in range(REQ_MAX + 1)]

    # goal
    goal_alp = alp
    goal_cop = cop
    for problem in problems:
        goal_alp = max(goal_alp, problem[0])
        goal_cop = max(goal_cop, problem[1])

    if goal_alp <= alp and goal_cop <= cop:
        return 0

    # init
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    dp[alp][cop] = 0

    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            for req_alp, req_cop, rw_alp, rw_cop, cost in problems:
                if i < req_alp or j < req_cop:
                    continue
                ni = min(i + rw_alp, goal_alp)
                nj = min(j + rw_cop, goal_cop)

                a = dp[i][j] + cost
                b = dp[ni][nj]
                dp[ni][nj] = min(dp[i][j] + cost, dp[ni][nj])

    answer = dp[goal_alp][goal_cop]
    return answer


# 예시 1
Q1 = {
    "alp": 10,
    "cop": 10,
    "problems": [
        [10, 15, 2, 1, 2],
        [20, 20, 3, 3, 4],
    ],
}

# 예시 2
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

# 대각선 지름길 추가
Q3 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [0, 0, 1, 1, 1],
        [150, 150, 1, 1, 100],
    ],
}

# 도착지 overflow
Q4 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [4, 3, 1, 1, 100],
        [0, 0, 2, 2, 1],
    ],
}

# 이미 완료된 조건이 있는 경우
Q5 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [0, 2, 1, 1, 100],
    ],
}

# 이미 완료된 조건이 있는 경우 2
Q6 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [2, 0, 1, 1, 100],
    ],
}

# 모든 조건이 완료된 경우
Q7 = {
    "alp": 2,
    "cop": 2,
    "problems": [
        [1, 1, 1, 1, 100],
    ],
}

# Q4와 비슷한 문제
Q8 = {
    "alp": 10,
    "cop": 10,
    "problems": [
        [0, 0, 5, 5, 1],
        [30, 10, 1, 1, 100],
    ],
}

# 탐색범위가 굉장히 커질 수 있는 요지를 해결했는가
Q9 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [0, 0, 30, 2, 1],
        [150, 150, 30, 30, 100],
    ],
}

print(solution(**Q1))
print(solution(**Q2))
print(solution(**Q3))
print(solution(**Q4))
print(solution(**Q5))
print(solution(**Q6))
print(solution(**Q7))
print(solution(**Q8))
print(solution(**Q9))
