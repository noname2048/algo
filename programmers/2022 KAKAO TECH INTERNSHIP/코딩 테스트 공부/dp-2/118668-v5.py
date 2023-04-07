# v4 로 부터 케이스를 몇개 더 추가


def solution(alp, cop, problems):
    DP_MAX = 90_000
    REQ_MAX = 150
    I_MAX = 181
    dp = [[DP_MAX] * I_MAX for _ in range(I_MAX)]

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
    for i in range(0, alp + 1):
        for j in range(0 , cop + 1):
            dp[alp][cop] = 0
    
    for i in range(alp, REQ_MAX + 1):
        for j in range(cop, REQ_MAX + 1):
            
            for req_alp, req_cop, rw_alp, rw_cop, cost in problems:
                if i < req_alp or j < req_cop:
                        continue
                ni = i + rw_alp
                nj = j + rw_cop
                dp[ni][nj] = min(dp[i][j] + cost, dp[ni][nj])
    
    answer = DP_MAX
    for  i in range(goal_alp, I_MAX):
        for j in range(goal_cop, I_MAX):
            answer = min(answer, dp[i][j])

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
        [150, 150, 1, 1, 150],
    ],
}

# 도착지 overflow
Q4 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [4, 3, 1, 1, 150],
        [0, 0, 2, 2, 1],
    ],
}

# 이미 완료된 조건이 있는 경우
Q5 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [0, 2, 1, 1, 150],
    ],
}

# 이미 완료된 조건이 있는 경우 2
Q6 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [2, 0, 1, 1, 150],
    ],
}

# 모든 조건이 완료된 경우
Q7 = {
    "alp": 2,
    "cop": 2,
    "problems": [
        [1, 1, 1, 1, 150],
    ],
}


# 단위 이동보다 좋은 조건이 있는 경우
Q8 = {
    "alp": 2,
    "cop": 2,
    "problems": [
        [0, 0, 0, 3, 1],
        [1, 1, 1, 1, 150],
    ],
}

Q9 = {
    "alp": 10,
    "cop": 10,
    "problems": [
        [0, 0, 5, 5, 1],
        [20, 10, 1, 1, 150],
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
