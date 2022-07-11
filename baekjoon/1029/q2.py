from sys import stdin

input = stdin.readline


def solve():
    n = int(input())
    m = []
    for _ in range(n):
        tmp = map(int, (input().strip()))
        m.append(list(tmp))

    bit_index = int("1" * n, 2) + 1
    # cache[node_index][visit_state][value]
    cache = [[[-1] * 10 for _ in range(bit_index)] for _ in range(15)]

    def re(here, visit, value) -> int:
        """방문한 곳, 현재 idx, 현재 가격을 통해 방문자 수를 리턴합니다."""
        if cache[here][visit][value] >= 0:
            return cache[here][visit][value]

        result = [0]
        for next in range(n):
            # 이미 방문한 경우
            if 1 << next & visit:
                continue
            # 지금 가격보다 같거나 비싸게 사줄 수 없다면
            if m[here][next] < value:
                continue

            tmp = re(next, visit | 1 << next, m[here][next])
            result.append(tmp)

        # 가장 많은 노드 수 선택
        cache[here][visit][value] = max(result) + 1
        return cache[here][visit][value]

    ans = re(0, 1, 0)
    print(ans)


if __name__ == "__main__":
    solve()
