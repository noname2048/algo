from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    INF = 200_000_000
    graph = defaultdict(dict)
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f

    def dijkstra(start, finish):
        dist = [INF] * (n + 1)

        q = []
        heapq.heappush(q, (0, start))  # (value, idx)
        while q:
            fee, idx = heapq.heappop(q)

            if dist[idx] < fee:
                continue

            for k in graph[idx].keys():
                if dist[k] > fee + graph[idx][k]:
                    dist[k] = fee + graph[idx][k]
                    heapq.heappush(q, (dist[k], k))

        return dist[finish]

    mn = INF
    for break_point in range(1, n + 1):
        s_ = 0 if break_point == s else dijkstra(s, break_point)
        a_ = 0 if break_point == a else dijkstra(break_point, a)
        b_ = 0 if break_point == b else dijkstra(break_point, b)
        local = s_ + a_ + b_
        if local < mn:
            mn = local
            # print(s_, a_, b_, break_point)

    return mn


# ans = solution(
#     6,
#     4,
#     6,
#     2,
#     [
#         [4, 1, 10],
#         [3, 5, 24],
#         [5, 6, 2],
#         [3, 1, 41],
#         [5, 1, 24],
#         [4, 6, 50],
#         [2, 4, 66],
#         [2, 3, 22],
#         [1, 6, 25],
#     ],
# )
ans = solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
print(ans)
