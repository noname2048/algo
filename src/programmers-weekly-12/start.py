import sys

def dfs(dungeons, tried, visited):

    local_max = 0
    for idx, (x, y) in enumerate(dungeons):
        if idx not in visited and tried >= x:
            visited[idx] = 1
            local_max = max(1 + dfs(dungeons, tried - y, visited), local_max)
            del visited[idx]

    return local_max


def solution(k, dungeons):
    dungeons.sort()
    dungeons.reverse() # DESC

    answer = dfs(dungeons, k, dict())
    return answer

if __name__ == "__main__":
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    print(solution(k, dungeons))
