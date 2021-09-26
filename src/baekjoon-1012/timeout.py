from collections import deque

# import sys

dir_yx_pos = {
    "up": [1, 0],
    "right": [0, 1],
    "down": [-1, 0],
    "left": [0, -1],
}


def label(board, target_idx=1):
    row, col = len(board), len(board[0])
    label = [[0] * col for _ in range(row)]
    label_count = 0

    for i in range(row):
        for j in range(col):
            if label[i][j] == 0 and board[i][j] == target_idx:

                label_count += 1
                queue = deque()
                queue.append([i, j])

                while queue:
                    y, x = queue.popleft()
                    label[y][x] = label_count

                    for dy, dx in dir_yx_pos.values():
                        ny = y + dy
                        nx = x + dx
                        if (
                            0 <= ny < row
                            and 0 <= nx < col
                            and label[ny][nx] == 0
                            and board[ny][nx] == target_idx
                        ):
                            queue.append([ny, nx])
    return label_count


# sys.stdin = open("input2.txt", "r")

for testcase in range(int(input())):
    m, n, k = list(map(int, input().split()))
    # 가로 1 ≤ M ≤ 50
    # 세로 1 ≤ N ≤ 50
    # 배추 수 1 ≤ K ≤ 2500

    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int, input().split()))
        board[y][x] = 1

    print(label(board))
