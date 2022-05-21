# 아침스터디
# 카카오 2022 블라인드 문제
# 파괴되지 않은 건물


def solution(board, skill):
    for s in skill:
        tf, sy, sx, ey, ex, amount = s

        up_down = 1 if tf == 2 else -1
        add = up_down * amount
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                board[y][x] += add
    answer = 0
    for row in board:
        for item in row:
            if item > 0:
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
