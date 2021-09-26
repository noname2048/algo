from collections import deque


debug = 1


def solution(game_board, table):
    answer = -1
    return answer


def rotate_clockwise(symbol):
    # if symbol is 2D, result will be deepcopy
    # a: list = reversed(symbol)
    # b = zip(*a)
    # c = [list(ele) for ele in b]
    # 잘못된 접근 방식으로는: list(zip(*reversed(symbol)))
    return [list(ele) for ele in zip(*reversed(symbol))]


game_board = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0],
]

table = [
    [1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
]

dir_yx_pos = {
    "up": [1, 0],
    "right": [0, 1],
    "down": [-1, 0],
    "left": [0, -1],
}


def make_pretty_2d(matrix):
    # for str_list in matrix:
    #   str_list = ["{:3}".format(item) for item in row]
    #   new_row = " ".join(str_list)

    return "\n".join(
        [" ".join(["{:3}".format(item) for item in row]) for row in matrix]
    )


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
    return label


labeled_board = label(game_board, 1)
empty_space = label(game_board, 0)
labeled_table = label(table, 1)

print("board")
print(make_pretty_2d(game_board), sep=None)
print("labled_board")
print(make_pretty_2d(labeled_board))
print("empty_space")
print(make_pretty_2d(empty_space))
print("table")
print(make_pretty_2d(table))
