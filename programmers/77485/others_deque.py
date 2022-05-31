from collections import deque


def solution(rows, columns, queries):
    arr = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a, b, c, d = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
        for x in range(d - b):
            answer.append(arr[a][b + x])
        for y in range(c - a):
            answer.append(arr[a + y][d])
        for z in range(d - b):
            answer.append(arr[c][d - z])
        for k in range(c - a):
            answer.append(arr[c - k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d - b):
            arr[a][b + x] = answer[0]
            answer.popleft()
        for y in range(c - a):
            arr[a + y][d] = answer[0]
            answer.popleft()
        for z in range(d - b):
            arr[c][d - z] = answer[0]
            answer.popleft()
        for k in range(c - a):
            arr[c - k][b] = answer[0]
            answer.popleft()
    return result
