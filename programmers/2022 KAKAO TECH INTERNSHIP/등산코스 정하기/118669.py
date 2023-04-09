# 13 부터 25까지 시간초과 혹은 런타임 에러
from collections import defaultdict


def solution(n, paths, gates, summits):
    """
    n: int, [2, 50_000]
    paths: List[List[int, int, int]]
    gates: List[int]
    summits: List[int]
    """
    node_set = set(range(1, n + 1))
    gate_set = set(gates)
    summit_set = set(summits)
    rest_set = node_set - gate_set - summit_set

    answer = [-1, 20_000_000, []]
    for gate in gates:
        for summit in summits:
            local_set = rest_set.copy()
            local_set.add(gate)
            local_set.add(summit)

            # local problem 에 쓰일 hash
            edge_hash = defaultdict(dict)
            visited = defaultdict(int)
            visited[gate] = 1

            for path in paths:
                a, b, intensity = path
                if a in local_set and b in local_set:
                    edge_hash[a][b] = intensity
                    edge_hash[b][a] = intensity

            def recur(here, i_list):
                nonlocal answer
                if here in summit_set:
                    max_intensity = max(i_list)
                    if answer[1] > max_intensity:
                        answer = [summit, max_intensity]
                    return

                for next in edge_hash[here].keys():
                    if visited[next] == 0:
                        visited[next] = 1
                        i_list.append(edge_hash[here][next])
                        recur(next, i_list)
                        i_list.pop()
                        visited[next] = 0

            recur(gate, [])

    return answer[0], answer[1]


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
    "n": 6,
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

print(solution(**Q1))
print(solution(**Q2))
print(solution(**Q3))
print(solution(**Q4))
