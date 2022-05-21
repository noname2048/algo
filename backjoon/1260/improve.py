from collections import deque

n, m, v = map(int, input().split())
node = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for ele in node:
    ele.sort(reverse=True)  # DESC


def dfs():
    visited = [0 for _ in range(n + 1)]
    path = []
    stack = [v]

    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = 1
            path.append(curr)

            for next in node[curr]:
                if not visited[next]:
                    stack.append(next)

    return path


def bfs():
    visited = [0 for _ in range(n + 1)]
    path = []
    queue = deque([v])

    while queue:
        curr = queue.popleft()
        if not visited[curr]:
            visited[curr] = 1
            path.append(curr)

            for next in reversed(node[curr]):
                if next in node[curr]:
                    queue.append(next)

    return path


print(" ".join(map(str, dfs())))
print(" ".join(map(str, bfs())))
