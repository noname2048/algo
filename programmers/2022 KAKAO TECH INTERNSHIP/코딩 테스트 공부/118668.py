cache = []
g_problems = []
start_alp = 0
target_alp = 0
start_cop = 0
target_cop = 0


def solution(alp, cop, problems):
    global cache
    global g_problems
    global start_alp, target_alp
    global start_cop, target_cop

    for problem in problems:
        rq_alp = problem[0]
        rq_cop = problem[1]

        if target_alp < rq_alp:
            target_alp = rq_alp
        if target_cop < rq_cop:
            target_cop = rq_cop

    start_alp = alp
    start_cop = cop

    basic_problem = [[0, 0, 0, 1, 1], [0, 0, 1, 0, 1]]
    g_problems.extend(basic_problem)
    g_problems.extend(problems)

    LIMIT = 151
    cache = [[-1] * LIMIT for _ in range(LIMIT)]
    for i in range(target_alp, LIMIT):
        for j in range(target_cop, LIMIT):
            cache[i][j] = 0

    answer = re(start_alp, start_cop)
    print(answer)
    return answer


def re(x, y):
    """재귀"""
    global cache
    global g_problems
    global start_alp, target_alp
    global start_cop, target_cop

    if not start_alp <= x <= 150 or not start_cop <= y <= 150:
        return float("inf")

    if target_alp <= x and target_cop <= y:
        return 0

    if cache[x][y] != -1:
        return cache[x][y]

    local_min = float("inf")
    for problem in g_problems:
        rq_alp = problem[0]
        rq_cop = problem[1]
        rw_alp = problem[2]
        rw_cop = problem[3]
        cost = problem[4]

        if x < rq_alp or y < rq_cop:
            continue

        new_cost = re(x + rw_alp, y + rw_cop) + cost
        if new_cost < local_min:
            local_min = new_cost

    cache[x][y] = local_min
    return cache[x][y]
