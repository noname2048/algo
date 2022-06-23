n, m = list(map(int, input().split()))
rect = [[] for _ in range(n)]
for i in range(n):
    rect[i] = list(map(int, list(input())))

# n, m = [3, 5]
# q = [
#     [4, 2, 1, 0, 1],
#     [2, 2, 1, 0, 0],
#     [2, 2, 1, 0, 1],
# ]


def solution(rect):
    n, m = len(rect), len(rect[0])
    ans = 0

    max_r = n if n < m else m

    for r in range(1, max_r):
        for row in range(n - r):
            for col in range(m - r):
                if row + r < n and col + r < m:
                    if (
                        rect[row + 0][col + 0]
                        == rect[row + 0][col + r]
                        == rect[row + r][col + 0]
                        == rect[row + r][col + r]
                    ):
                        ans = max(ans, r)

    return (ans + 1) ** 2


print(solution(rect))
