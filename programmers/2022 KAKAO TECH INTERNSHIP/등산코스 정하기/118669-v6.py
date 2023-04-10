# v5 를 heap 으로 교체
# heap queue 가 더 성능이 좋을 줄 알았는데 v5 가 의외로 성능이 좋게 나옴 (시행횟수 2)
# 가장 시간이 많이 걸린 21번 문제에 대해서
# v5는 323ms, v6는 455ms
# 그 다음 시간이 많이 걸린 마지막 문제에 대해서
# v5는 465, v6는 455

from collections import defaultdict
from heapq import heappush, heappop


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
    visited = [False] * (n + 1)
    queue = []

    for gate in gates:
        cost[gate] = 0  # 시작점 0으로 초기화
        heappush(queue, (0, gate))

    while queue:
        _, here = heappop(queue)
        if visited[here] == True:
            continue
        
        visited[here] = True
        for next, intensity in edge_hash[here].items():
            new_cost = max(cost[here], intensity)
            if cost[next] > new_cost:
                cost[next] = new_cost
                heappush(queue, (new_cost, next))

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
