import sys
from matrix_utils import make_pretty_2d

sys.stdin = open("input.txt", "r")


class DFSStack:
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    def __init__(self, board):
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
        self.labled_board = [[0] * self.col for _ in range(self.row)]
        self.label_cnt = 0

    def stack_dfs(self, y, x):
        stack = []
        stack.append([y, x])

        while stack:
            ty, tx = stack.pop()
            self.labled_board[ty][tx] = self.label_cnt

            for idx in [3, 2, 1, 0]:
                next_y = ty + self.dy[idx]
                next_x = tx + self.dx[idx]

                if (
                    0 <= next_y < self.row
                    and 0 <= next_x < self.col
                    and self.board[y][x] == 1
                    and self.labled_board[y][x] == 0
                ):
                    stack.append([next_y, next_x])

    def calc(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == 1 and self.labled_board[i][j] == 0:
                    self.label_cnt += 1
                    self.stack_dfs(i, j)

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

    dfs_handler = DFSStack(board)
    print(dfs_handler.calc())
    print(make_pretty_2d(dfs_handler.labled_board))
