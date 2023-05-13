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
    answer = solve01(edges)
    answer = max(answer, solve02(n, m, edges))
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
    edge_dict = defaultdict(dict)
    for idx, edge in edges:
        u, v, d = edge
        edge_dict[u] = (idx, d)
        edge_dict[v] = (idx, d)

    for idx, edge in enumerate(edges):
        # 정점 u 에서 v 를 제외하고 간선이 1개 이상인가
        a, b, d = edge
        a_dict = {k: v for k, v in edge_dict[u].items() if k != b}
        b_dict = {k: v for k, v in edge_dict[v].items() if k != a}
        a_dict = sorted(a_dict)
        b_dict = sorted(b_dict)


        edge_candidate = set()
        for i, d, in edge_dict[u]:
            if i != idx:
                edge_candidate.add((i, d))
            
        for j, d in edge_dict[v]:
            if j != idx:
                edge_candidate.add((j, d))


        edge_candidate = set()
        for i, d in edge_dict[u]:
            edge_candidate.add((i, d))
        for j, u, d in edge_dict[v]:
            edge_candidate.add((j, d))
        edge_candidate.remove((idx, edge[2]))

        # 간선이 사이클을 이루는 경우 밖에 없는 경우 제외
        if len(edge_candidate) < 2:
            continue

        # 


    for node in edge_dict.keys():
        edge_dict[node] = dict(sorted(edge_dict[node].items(), key=lambda x: x[1], reverse=True))
    
    for edge in edges:
        local_answer = -1
        u, v, d = edge
        result_u = [(-1, 0), (-1, 0)]
        result_v = [(-2, 0), (-2, 0)]

        local_u = {k: v for k, v in edge_dict[u].items() if k != v}   
        local_v = {k: v for k, v in edge_dict[v].items() if k != u}

        u_keys = list(local_u.keys())
        u_values = list(local_u.values())
        v_keys = list(local_v.keys())
        v_values = list(local_v.values())

        if len(u_keys) > 0:
            result_u[0] = (u_keys[0], u_values[0])
        if len(u_keys) > 1:
            result_u[1] = (u_keys[1], u_values[1])

        if len(v_keys) > 0:
            result_v[0] = (v_keys[0], v_values[0])
        if len(v_keys) > 1:
            result_v[1] = (v_keys[1], v_values[1])
        
        if result_u[0][0] == result_v[0][0]:
            a = result_u[0][1] + result_v[1][1]
            b = result_v[0][1] + result_u[1][1]
            local_answer = max(a, b)
        else:
            local_answer = result_u[0][1] + result_v[0][1]
        answer = max(answer, local_answer + d)

    return answer

main()
