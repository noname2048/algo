# https://www.acmicpc.net/source/58252486
# 위의 코드를 참고하여 변형함
# 속도 측정시 더 빠른가 비교를 위해 제출
# 결과는.. 많이 빨라지지 않았다.

import sys
from collections import deque

sys.stdin = open("p2.txt", "r")
input = lambda: sys.stdin.readline().rstrip()


def solve() -> None:
    n: int = int(input())
    graph: list = [[] for i in range(n + 1)]

    for i in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    a, b, c = map(int, input().split())
    q = deque([(a, "a"), (b, "b"), (c, "c")])

    visit = [0] * (n + 1)
    visit[a] = 1
    visit[b] = visit[c] = -1

    while q:
        node, token = q.popleft()
        if token == "a":  # 도둑차례
            # 현재 위치가 리프노드라면
            if len(graph[node]) == 1:
                return "YES"

            # 경찰이 점령한 곳이라면
            if visit[node] == -1:
                continue

            # 다음 후보지를 고려한다
            for next in graph[node]:
                if visit[next]:  # 0만 점령 시도
                    continue
                else:
                    visit[next] = 1
                    q.append((next, token))

        else:  # 경찰차례
            for next in graph[node]:
                if visit[next] != -1:  # 1과 0을 점령
                    visit[next] = -1
                    q.append((next, token))

    return "NO"


print(solve())
