def solution(rows, columns, queries):
    matrix = [
        list(range(r * columns + 1, r * columns + columns + 1)) for r in range(rows)
    ]

    ans = []
    for x1, y1, x2, y2 in queries:
        arr = (
            matrix[x1 - 1][y1 - 1 : y2]
            + [matrix[i][y2 - 1] for i in range(x1 - 1, x2)][1:-1]
            + matrix[x2 - 1][y1 - 1 : y2][::-1]
            + [matrix[i][y1 - 1] for i in range(x1 - 1, x2)][::-1][1:-1]
        )
        ans.append(min(arr))

        arr = [arr[-1]] + arr[:-1]
        a, b, c, d = (
            arr[: y2 - y1 + 1],
            arr[y2 - y1 + 1 : y2 - y1 + x2 - x1],
            arr[y2 - y1 + x2 - x1 : y2 - y1 + x2 - x1 + y2 - y1 + 1],
            arr[y2 - y1 + x2 - x1 + y2 - y1 + 1 :],
        )
        matrix[x1 - 1][y1 - 1 : y2] = a
        matrix[x2 - 1][y1 - 1 : y2] = c[::-1]

        matrix = list(map(list, zip(*matrix)))
        matrix[y2 - 1][x1 : x2 - 1] = b
        matrix[y1 - 1][x1 : x2 - 1] = d[::-1]
        matrix = list(map(list, zip(*matrix)))
    return ans
