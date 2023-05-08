# 순환이 가능한 그래프 구조에서
# dfs 로 길이만큼 탐색했을 때
# 가장 cost 가 큰 경로는?
# 딘, 경로가 4보다 짧을 수 있다.
# 라고 하면, 단순 dfs 로는 풀 수 없음
# 어떤 점이던, 나와 연결된 선분의 개수는 2개가 최대 여야 함
# (양 옆이므로)

# 그리디로 풀 수 있는 문제인가?
# 블가?
# 4명의 학생만을 선발하는 것에 유의해보자
# 완전 탐색은 절대 불가
# 가능한 후보군들을 완전 탐색한다면?  300_000C4
# 대략적으로 300_000 ** 4 / 24  = 역시 너무 큰 수

import sys
from collections import defaultdict

sys.stdin = open("p1.txt", "r")
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = list(map(int, input().split()))
    edges = defaultdict(dict)
    for _ in range(m):
        u, v, d = list(map(int, input().split()))
        edges[u][v] = d
        edges[v][u] = d

    cost = 0
    visited = {}
    cache = {}
    conn = 0
    for u in edges.keys():
        cost = max(cost, get_cost(u, visited, cache, conn))

# 연결될 수 있는 시너지 한에서만 모두 고려해보자
def get_cost(here, visited, cache, conn):
    # 현제 연결된 수 4개 이상
    if conn > 4:
        return 0
    cache = {}
    global synergy_arr
    next = synerge_candidate[0]
    if cache[next] > 2 and cache[start] > 2:
        return 0
    else:
        get_cost(here, visited, cache, conn)
