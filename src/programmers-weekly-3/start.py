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
