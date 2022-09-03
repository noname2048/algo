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


def parse_grid(board):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(board).items():
        if d in digits and not assign(values, s, d):
            return False
    return values


def assign(values, s, d):
    other_values = values[s].replace(d, "")
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
