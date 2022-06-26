# others.py를 확인 후에 다시 정리
from sys import stdin

input = stdin.readline
INF = float("inf")


def solve():
    tc = int(input())  # testcase
    y, x = [0] * 20, [0] * 20
    ans, ty, tx = INF, 0, 0  # answer, total_y, total_x

    def comb(cnt, idx, sy, sx):
        """Make combination by recursions

        :param int cnt: counter
        :param int idx: index for starting dfs
        :param list[int] sy: sub_y, for subtraction
        :param list[int] sx: sub_x
        """
        nonlocal ans
        if cnt == 0:
            tmp = (ty - 2 * sy) ** 2 + (tx - sx * 2) ** 2
            if ans > tmp:
                ans = tmp
            return

        for i in range(idx, n - cnt + 1):
            comb(cnt - 1, i + 1, sy + y[i], sx + x[i])

    for _ in range(tc):
        n = int(input())
        ans, ty, tx = INF, 0, 0

        for j in range(n):
            y[j], x[j] = map(int, input().split())
            ty += y[j]
            tx += x[j]

        # 0번 인덱스를 무조건 subtraction에 포함시킴니다.
        # 상관없는 이유는 거리이기 때문에
        comb(n // 2 - 1, 1, y[0], x[0])
        print(ans**0.5)


if __name__ == "__main__":
    solve()
