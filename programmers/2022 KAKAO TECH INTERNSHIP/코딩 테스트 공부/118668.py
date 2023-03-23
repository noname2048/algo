cache = []
g_problems = []
mx_alp = 0
mx_cop = 0

def solution(alp, cop, problems):
    global cache
    global g_problems
    global mx_alp
    global mx_cop

    basic_problem = [[0, 0, 0, 1, 1], [0, 0, 1, 0, 1]]
    g_problems.extend(basic_problem)
    g_problems.extend(problems)
    cache = [[-1] * 151 for _ in range(151)]

    mx_alp = 0
    mx_cop = 0

    for problem in problems:
        rq_alp = problem[0]
        rq_cop = problem[1]

        if mx_alp < rq_alp:
            mx_alp = rq_alp
        if mx_cop < rq_cop:
            rq_cop = rq_cop

    answer = re(mx_alp, mx_cop)
    print(answer)
    return answer


def re(x, y):
    """재귀"""
    global cache
    global g_problems
    global mx_alp
    global mx_cop

    if not 0 <= x <= 150 or not 0 <= y <= 150:
        return float("inf")

    if cache[x][y] != -1:
        return cache[x][y]

    local_min = float("inf")
    for problem in g_problems:
        problem_alp = problem[0]
        problem_cop = problem[1]
        reward_alp = problem[2]
        reward_cop = problem[3]
        problem_cost = problem[4]

        if x < problem_alp or y < problem_cop:
            continue

        new_cost = re(x + reward_alp, y + reward_cop) + problem_cost
        if new_cost < local_min:
            local_min = new_cost
    
    with open(f"log/{x:03d}_{y:03d}.txt", mode="w+") as f:
        for i in range(mx_alp)
        f.write(f"{num:03d}" for num in cache[x])       

    cache[x][y] = local_min
    return cache[x][y]


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

solution(**Q1)
