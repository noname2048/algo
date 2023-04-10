# v4 에서 dij 를 완성시키지 못한 고질적인 문제 발견
from collections import defaultdict


def solution(n, paths, gates, summits):
    # 초기설정
    summits.sort()
    node_type = ["-"] * (n + 1)
    for gate in gates:
        node_type[gate] = "g"
    for summit in summits:
        node_type[summit] = "s"

    edge_hash = defaultdict(dict)
    for a, b, intensity in paths:
        if node_type[a] != "s" and node_type[b] != "g":
            edge_hash[a][b] = intensity
        if node_type[b] != "s" and node_type[a] != "g":
            edge_hash[b][a] = intensity

    cost = [float("inf")] * (n + 1)  # minma intensity of reaching node
    next_list = {}

    for gate in gates:
        cost[gate] = 0  # 시작점 0으로 초기화
        next_list[gate] = True

    while next_list.keys():
        new_next_list = {}
        for here in next_list:
            for next, intensity in edge_hash[here].items():
                new_cost = max(cost[here], intensity)
                if cost[next] > new_cost:
                    cost[next] = new_cost
                    new_next_list[next] = True

        next_list = new_next_list

    answer = [-1, float('inf')]
    for summit in summits:
        if answer[1] > cost[summit]:
            answer = [summit, cost[summit]]

    return answer


Q1 = {
    "n": 6,
    "paths": [
        [1, 2, 3],
        [2, 3, 5],
        [2, 4, 2],
        [2, 5, 4],
        [3, 4, 4],
        [4, 5, 3],
        [4, 6, 1],
        [5, 6, 1],
    ],
    "gates": [1, 3],
    "summits": [5],
    # "result": [5, 3],
}

Q2 = {
    "n": 7,
    "paths": [
        [1, 4, 4],
        [1, 6, 1],
        [1, 7, 3],
        [2, 5, 2],
        [3, 7, 4],
        [5, 6, 6],
    ],
    "gates": [1],
    "summits": [2, 3, 4],
    # "result": [3, 4],
}

Q3 = {
    "n": 7,
    "paths": [
        [1, 2, 5],
        [1, 4, 1],
        [2, 3, 1],
        [2, 6, 7],
        [4, 5, 1],
        [5, 6, 1],
        [6, 7, 1],
    ],
    "gates": [3, 7],
    "summits": [1, 5],
    # "result": [5, 1],
}

Q4 = {
    "n": 6,
    "paths": [
        [1, 3, 10],
        [1, 4, 20],
        [2, 3, 4],
        [2, 4, 6],
        [3, 5, 20],
        [4, 5, 6],
    ],
    "gates": [1, 2],
    "summits": [5],
    # "result": [5, 6],
}

Q5 = {
    "n": 11,
    "paths": [
        [1, 2, 2],
        [2, 4, 2],
        [4, 6, 2],
        [6, 8, 2],
        [8, 10, 2],
        [1, 3, 2],
        [3, 5, 2],
        [5, 7, 2],
        [7, 9, 2],
        [9, 11, 2],
        [3, 8, 200],
    ],
    "gates": [1],
    "summits": [10, 11],
}

print(solution(**Q1))
print(solution(**Q2))
print(solution(**Q3))
print(solution(**Q4))
print(solution(**Q5))
