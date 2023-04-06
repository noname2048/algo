# I_MAX 도입으로 런타임 에러 해결
# 여전히 실패가 있음
# 결과값 갱신에 if 문 추가하여 Q4 케이스 해결

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

    # problem
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    # init
    dp[alp][cop] = 0
    answer = DP_MAX

    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            for req_alp, req_cop, rw_alp, rw_cop, cost in problems:
                if i < req_alp or j < req_cop:
                    continue
                ni = i + rw_alp
                nj = j + rw_cop

                dp[ni][nj] = min(dp[i][j] + cost, dp[ni][nj])
                if ni >= goal_alp and nj >= goal_cop:
                    answer = min(dp[ni][nj], answer)

    return answer

Q4 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [4, 3, 1, 1, 150],
        [0, 0, 2, 2, 1],
    ],
}
solution(**Q4) 
