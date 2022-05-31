def solution(rows, columns, querises):
    big_table = [[0 for _ in range(columns)] for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            big_table[r][c] = (c + 1) + columns * r

    def rotate(x1, y1, x2, y2):
        nonlocal big_table
        temp = big_table[x1][y2]
        mn = temp

        # right
        for y in range(y2, y1, -1):
            big_table[x1][y] = big_table[x1][y - 1]
            mn = min(big_table[x1][y], mn)
        # up
        for x in range(x1, x2):
            big_table[x][y1] = big_table[x + 1][y1]
            mn = min(big_table[x][y1], mn)

        # left
        for y in range(y1, y2):
            big_table[x2][y] = big_table[x2][y + 1]
            mn = min(big_table[x2][y], mn)

        # up
        for x in range(x2, x1 + 1, -1):
            big_table[x][y2] = big_table[x - 1][y2]
            mn = min(big_table[x][y2], mn)

        big_table[x1 + 1][y2] = temp
        return mn

    answer = []
    for query in querises:
        x1a, y1a, x2a, y2a = query
        x1, y1, x2, y2 = x1a - 1, y1a - 1, x2a - 1, y2a - 1
        local = rotate(x1, y1, x2, y2)
        answer += [local]

    return answer


def test_1():
    rows = 6
    columns = 6
    queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    result = [8, 10, 25]

    assert result == solution(rows, columns, queries)


def test_2():
    rows = 3
    columns = 3
    queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
    result = [1, 1, 5, 3]

    assert result == solution(rows, columns, queries)


def test_3():
    rows = 100
    columns = 97
    queries = [[1, 1, 100, 97]]
    result = [1]

    assert result == solution(rows, columns, queries)
