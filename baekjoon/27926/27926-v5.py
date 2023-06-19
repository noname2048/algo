# v3 를 어떻게 더 개선할 수 있는가
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
    # 모든 간선마다 3개 순위의 간선을 저장
    for i, edge in enumerate(edges):
        u, v, d = edge
        adj[u].append((i, v, d))
        adj[v].append((i, u, d))

    answer = 0
    for idx, edge in enumerate(edges):
        u, v, d = edge
        # 정점이 각각 고려할 수 있는 간선이 있는가 확인
        if len(adj[u]) < 2 or len(adj[v]) < 2:
            continue

        # top 2개 뽑기
        u_cand = [(-1, -1, 0), (-1, -1, 0)]
        v_cand = [(-1, -1, 0), (-1, -1, 0)]

        for k in range(2):
            u_max = -1
            for e in adj[u]:
                if (
                    e[0] != idx  # 현재 고려하는 간선이 아닐것
                    and u_max < e[2]  #  가장 큰 간선이어야 가
                    and u_cand[0][0] != e[0]  # 2 위일떄 는 1위가 아니여야 함
                ):
                    u_cand[k] = e
                    u_max = e[2]

        for k in range(2):
            v_max = -1
            for e in adj[v]:
                if e[0] != idx and v_max < e[2] and v_cand[0][0] != e[0]:
                    v_cand[k] = e
                    v_max = e[2]

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
