board = [[0] * 9 for _ in range(9)]


def cross(A, B):
    return [a + b for a in A for b in B]


digits = "123456789"
rows = "ABCDEFGHI"
cols = digits

squares = cross(rows, cols)
unitlist = (
    [cross(rows, c) for c in cols]
    + [cross(r, cols) for r in rows]
    + [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
)
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)


def grid_values(board):
    chars = []
    for l in board:
        temp = [c for c in l if c in digits or c in "0."]
        chars += temp
    return dict(zip(squares, chars))
