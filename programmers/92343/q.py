# 22-05-13

# 무한루프 아침 스터디
# 카카오 블라인드 2022 양과늑대
from collections import defaultdict


g_sheep = 1


def solution(info, edges):
    edge_dict = defaultdict(set)
    for edge in edges:
        pa, ch = edge
        edge_dict[pa].add(ch)

    init_state = 0b1
    re(state=init_state, info=info, edge_dict=edge_dict, sheep=1, wolf=0)
    answer = g_sheep
    return answer


def find_cand(state, edge_dict: dict):
    ret = []

    def dfs(cand, idx):
        # find available candidates with dfs
        for child in edge_dict[idx]:
            if state | (1 << child) != state:  # 방문하지 않았으면
                cand += [child]
            else:  # 방문했으면
                dfs(cand, child)

    dfs(ret, 0)
    return ret


def re(state: int, info, edge_dict, sheep, wolf):
    global g_sheep

    # 최고값 갱신
    g_sheep = max(g_sheep, sheep)

    # 현재 상태에서 연결될 수 있는 edges 들을 검토
    candidates = find_cand(
        state=state,
        edge_dict=edge_dict,
    )

    # set 중에서 양인것을 앞쪽으로 빼기
    sheeps = [candidate for candidate in candidates if info[candidate] == 0]
    wolfes = [candidate for candidate in candidates if info[candidate] == 1]
    new_candidates = sheeps + wolfes

    # 방문할 수 있으면 방문하기
    for candidate in new_candidates:
        if info[candidate] == 0:
            new_state = state | (0b1 << candidate)
            re(new_state, info, edge_dict, sheep + 1, wolf)

        else:
            if sheep > wolf + 1:
                new_state = state | (1 << candidate)
                re(new_state, info, edge_dict, sheep, wolf + 1)
            else:
                # 늑대가 많으면 탐색 중단
                pass


if __name__ == "__main__":
    # q1 = {
    #     "info": [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    #     "edges": [
    #         [0, 1],
    #         [1, 2],
    #         [1, 4],
    #         [0, 8],
    #         [8, 7],
    #         [9, 10],
    #         [9, 11],
    #         [4, 3],
    #         [6, 5],
    #         [4, 6],
    #         [8, 9],
    #     ],
    # }
    # a1 = 5
    # s1 = solution(q1["info"], q1["edges"])
    # print(s1)
    # assert a1 == s1
    q2_info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    q2_edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [1, 4],
        [2, 5],
        [2, 6],
        [3, 7],
        [4, 8],
        [6, 9],
        [9, 10],
    ]
    s2 = solution(q2_info, q2_edges)
    print(s2)
