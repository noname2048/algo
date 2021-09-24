from collections import deque


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


game_borad = [
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


def label_table(table):
    row = len(table)
    col = len(table[0])
    label = [[0 for _ in range(col)] for _ in range(row)]
    label_count = 0

    for i in range(row):
        for j in range(col):
            if label[i][j] == 0 and table[i][j] == 1:

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
                            and table[ny][nx] == 1
                        ):
                            queue.append([ny, nx])

    return table


def make_pretty_2d(matrix):
    # for str_list in matrix:
    #   str_list = ["{:3}".format(item) for item in row]
    #   new_row = " ".join(str_list)

    return "\n".join(
        [" ".join(["{:3}".format(item) for item in row]) for row in matrix]
    )


labeled = label_table(table)
print(make_pretty_2d(table))
print("---")
print(make_pretty_2d(labeled))
