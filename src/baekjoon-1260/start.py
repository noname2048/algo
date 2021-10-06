# import sys

# sys.stdin = open("input3.txt", "r")
#
from collections import deque

n, m, v = map(int, input().split())
node = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def dfs():
    global node

    visited = {}
    path = []
    stack = [v]

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited[curr] = 1
            path.append(curr)

            node[curr].sort(reverse=True)  # DESC
            for next in node[curr]:
                if next not in visited:
                    stack.append(next)

    return path


def bfs():
    global node

    visited = {}
    path = []
    queue = deque([v])

    while queue:
        curr = queue.popleft()
        if curr not in visited:
            visited[curr] = 1
            path.append(curr)

            node[curr].sort()  # ASC
            for next in node[curr]:
                if next not in visited:
                    queue.append(next)

    return path


print(dfs())
print(bfs())
