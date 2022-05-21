from collections import deque
import sys
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


for testcase in range(int(input())):
    m, n, k = list(map(int, input().split()))
    # 가로 1 ≤ M ≤ 50
    # 세로 1 ≤ N ≤ 50
    # 배추 수 1 ≤ K ≤ 2500

    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int, input().split()))
        board[y][x] = 1

    dfs_handler = DfsLabel(board, 1)
    print(dfs_handler.calc())
