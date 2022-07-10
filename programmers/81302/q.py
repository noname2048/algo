from sys import stdin

input = stdin.readline
keep_distance = False


def check_inboard(a, y, x, b):
    return a <= y < b and a <= x < b


def check_perpendicular(place, y, x):
    global keep_distance
    k = len(place)
    # UP, RIGHT, DOWN, LEFT
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    if place[y][x] == "P":

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if check_inboard(0, ny, nx, k):
                if place[ny][nx] == "P":
                    keep_distance = False
                    break

            more_y = ny + dy[i]
            more_x = nx + dx[i]

            if check_inboard(0, more_y, more_x, k):
                if place[more_y][more_x] == "P":
                    if place[ny][nx] != "X":
                        keep_distance = False
                        break

            # diagnal
            v1 = i
            v2 = (i + 1) % 4

            ay = y + dy[v1]
            ax = x + dx[v1]

            by = y + dy[v2]
            bx = x + dx[v2]

            diagonal_y = ay + dy[v2]
            diagonal_x = ax + dx[v2]

            if check_inboard(0, diagonal_y, diagonal_x, k):
                if place[diagonal_y][diagonal_x] == "P":
                    if place[ay][ax] != "X" or place[by][bx] != "X":
                        keep_distance = False
                        break


def solution(places):
    global keep_distance
    ans = []
    for idx, place in enumerate(places):
        keep_distance = True

        k = len(place)
        m = []

        for p in place:
            m.append(list(p))

        for i in range(k):
            for j in range(k):
                check_perpendicular(m, i, j)
                if not keep_distance:
                    break
            if not keep_distance:
                break

        if keep_distance:
            ans.append(1)
        else:
            ans.append(0)

    return ans


if __name__ == "__main__":
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]

    ans = solution(places)
    print(ans)
