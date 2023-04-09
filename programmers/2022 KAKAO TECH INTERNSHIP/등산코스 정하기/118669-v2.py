# v1 으로 부터 좀더 효율적인 알고리즘 작성
from collections import defaultdict


def solution(n, paths, gates, summits):
    answer = [-1, 20_000_000]
    edge_hash = defaultdict(dict)
    visited = defaultdict(int)

    def recur(here, goal, i_list):
        nonlocal answer
        nonlocal edge_hash
        nonlocal gates
        nonlocal summits
        nonlocal visited

        if here == goal:
            local_answer = max(i_list)
            if answer[1] > local_answer:
                answer = [goal, local_answer]
            return

        for next in edge_hash[here].keys():
            if visited[next] == 1:
                continue

            visited[next] = 1
            i_list.append(edge_hash[here][next])
            recur(next, goal, i_list)
            i_list.pop()
            visited[next] = 0

    for a, b, intensity in paths:
        edge_hash[a][b] = intensity
        edge_hash[b][a] = intensity

    visited.update({gate: 1 for gate in gates})
    visited.update({summit: 1 for summit in summits})
    for gate in gates:
        for summit in summits:
            visited[summit] = 0
            recur(gate, summit, [])
            visited[summit] = 1

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
