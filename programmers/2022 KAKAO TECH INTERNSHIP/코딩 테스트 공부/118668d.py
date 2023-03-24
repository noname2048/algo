from datetime import datetime, timedelta, timezone

KST = timezone(offset=timedelta(hours=9))


cache = []
g_problems = []
start_alp = 0
target_alp = 0
start_cop = 0
target_cop = 0

f = open(f"{datetime.now(tz=KST).strftime('%d-%H-%M-%S')}.txt", "+w", encoding="utf-8")


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
    cache = [[-1] * 151 for _ in range(151)]
    cache[target_alp][target_cop] = 0

    answer = re(start_alp, start_cop)
    print(answer)
    return answer


def re(x, y):
    """재귀"""
    global cache
    global g_problems
    global start_alp, target_alp
    global start_cop, target_cop

    if not start_alp <= x <= target_alp or not start_cop <= y <= target_cop:
        return float("inf")

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

    # with open(f"log/{x:03d}_{y:03d}.txt", mode="w+") as f:
    #     for i in range(mx_alp)
    #     f.write(f"{num:03d}" for num in cache[x])

    cache[x][y] = local_min

    f.write(f"---{x:3d}---{y:3d}---{local_min:4d}\n")
    for i in range(start_alp, target_alp + 1):
        line = (
            "  ".join(f"{int(num):3d}" for num in cache[i][start_cop:target_cop + 1]) + "\n"
        )
        f.write(line)
    f.write("\n")

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

solution(**Q2)
