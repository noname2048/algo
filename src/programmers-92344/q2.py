# 아침스터디
# 카카오 2022 블라인드 문제
# 파괴되지 않은 건물


def solution(board, skill):
    row = len(board)
    col = len(board[0])

    z_board = [[0] * col for _ in range(row)]

    for s in skill:
        tf, sy, sx, ey, ex, amount = s

        up_down = 1 if tf == 2 else -1
        add = up_down * amount
        z_board[sy][sx] += add
        if ex + 1 < col:
            z_board[sy][ex + 1] -= add
        if ey + 1 < row:
            z_board[ey + 1][sx] -= add
        if ex + 1 < col and ey + 1 < row:
            z_board[ey + 1][ex + 1] += add

    for r in z_board:
        for x in range(col - 1):
            r[x + 1] += r[x]

    for x in range(col):
        for y in range(row - 1):
            z_board[y + 1][x] += z_board[y][x]

    answer = 0
    for r in range(row):
        for c in range(col):
            if z_board[r][c] + board[r][c] > 0:
                answer += 1

    return answer


if __name__ == "__main__":
    q1_board = [
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5],
    ]
    q1_skill = [
        [1, 0, 0, 3, 4, 4],
        [1, 2, 0, 2, 3, 2],
        [2, 1, 0, 3, 1, 2],
        [1, 0, 1, 3, 3, 1],
    ]
    q1_answer = 10

    print(solution(q1_board, q1_skill))
