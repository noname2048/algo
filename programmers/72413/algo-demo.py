import math

f = open("weight.txt", "w+")


def print_matrix(m, memo=""):
    global f
    print(f"---{memo}", file=f)
    for i in range(len(m)):
        temp = ", ".join(map(lambda x: str(x).rjust(3, " "), m[i]))
        print(f"[{temp}]", file=f)


def solution(n, s, a, b, fares):
    # floyd warshall
    weight = [[math.inf] * n for _ in range(n)]

    for c, d, f in fares:
        weight[c - 1][d - 1] = f
        weight[d - 1][c - 1] = f

    for i in range(n):
        weight[i][i] = 0

    print_matrix(weight, "init")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if weight[j][k] > weight[j][i] + weight[i][k]:
                    weight[j][k] = weight[j][i] + weight[i][k]

        print_matrix(weight, f"i({i})")


ans = solution(
    6,
    4,
    6,
    2,
    [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ],
)

f.close()
