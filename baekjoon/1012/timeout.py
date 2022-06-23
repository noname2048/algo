from collections import deque

import sys

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


from copy import deepcopy


class DfsLabel:
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]

    def __init__(self, board, target_idx=1):
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        self.lable_board = [[0] * self.col for _ in range(self.row)]
        self.label_cnt = 0

    def dfs(self, y, x):
        self.lable_board[y][x] = self.label_cnt

        for idx in range(4):
            dy = y + self.dir_y[idx]
            dx = x + self.dir_x[idx]

            if (
                0 <= dy < self.row
                and 0 <= dx < self.col
                and self.board[dy][dx] == 1
                and self.lable_board[dy][dx] == 0
            ):
                self.dfs(dy, dx)

    def calc(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == 1 and self.lable_board[i][j] == 0:
                    self.label_cnt += 1
                    self.dfs(i, j)

        return self.label_cnt


sys.stdin = open("input2.txt", "r")

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

    dfs_handler = DfsLabel(board, 1)
    print(dfs_handler.calc())
