import sys

n, m, v = map(int, sys.stdin.readline().split())
node = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

for ele in node:
    ele.sort(reverse=True)  # DESC


def dfs():
    visited = {}
    path = []
    stack = [v]

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited[curr] = 1
            path.append(curr)

            stack += node[curr]

    return path


def bfs():
    visited = {}
    visited[v] = 1
    path = []
    queue = [v]

    while queue:
        curr = queue.pop()
        path.append(curr)

        for next in reversed(node[curr]):
            if next not in visited:
                visited[next] = 1
                queue = [next] + queue

    return path


print(" ".join(map(str, dfs())))
print(" ".join(map(str, bfs())))
