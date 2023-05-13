# v2의 timeout 을 더 효과적으로 대처해보자.
import sys
from collections import defaultdict

sys.stdin = open("p2.txt", "r")
input = lambda: sys.stdin.readline().rstrip()


def main():
    edges = []
    n, m = list(map(int, input().split()))
    for _ in range(m):
        u, v, d = list(map(int, input().split()))
        edges.append((u, v, d))

    a = solve01(edges)
    b = solve02(n, m, edges)
    answer = max(a, b)
    print(answer)


def solve01(edges):
    # case 01
    poped = {}
    for _ in range(2):
        temp_max = -1
        temp_idx = -1
        for idx, edge in enumerate(edges):
            _, _, d = edge
            if temp_max < d and idx not in poped:
                temp_max = d
                temp_idx = idx
        poped[temp_idx] = temp_max
    answer = sum(poped.values())
    return answer


def solve02(n, m, edges):
    # case 02
    adj = defaultdict(list)
    for i, edge in enumerate(edges):
        u, v, d = edge
        adj[u].append((i, v, d))
        adj[v].append((i, u, d))

    for node in adj.keys():
        adj[node] = list(sorted(adj[node], key=lambda x: x[2], reverse=True))

    answer = 0
    for idx, edge in enumerate(edges):
        u, v, d = edge
        # 정점이 각각 고려할 수 있는 간선이 있는가 확인
        if len(adj[u]) < 2 or len(adj[v]) < 2:
            continue

        # 지금 고려하고 있는 간선을 후보군에서 제거
        u_adj = [e for e in adj[u] if e[0] != idx]
        v_adj = [e for e in adj[v] if e[0] != idx]

        # 각 정점에서 2개 후보군을 뽑는다.
        u_cand = [u_adj[0], (-1, -1, 0)]
        v_cand = [v_adj[0], (-1, -1, 0)]

        if len(u_adj) > 1:
            u_cand[1] = u_adj[1]
        if len(v_adj) > 1:
            v_cand[1] = v_adj[1]

        # 각 정점의 가장 큰 후보의 타겟이 같지 않다면 활용
        if u_cand[0][1] != v_cand[0][1]:
            local_answer = u_cand[0][2] + v_cand[0][2] + d
        else:
            a = u_cand[0][2] + v_cand[1][2] + d
            b = u_cand[1][2] + v_cand[0][2] + d
            local_answer = max(a, b)

        answer = max(answer, local_answer)
    return answer


main()
