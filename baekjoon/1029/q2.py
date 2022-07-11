from sys import stdin

input = stdin.readline


def solve():
    n = int(input())
    m = []
    for _ in range(n):
        tmp = list(input().strip())
        tmp = list(map(int, tmp))
        m.append(tmp)

    cache = []

    def re(index, visited, last_price):
        arr = [0]
        for idx, v in enumerate(m[index]):
            if not visited[idx] and v >= last_price:
                visited[idx] = True
                tmp = re(idx, visited, v)
                arr.append(tmp)
                visited[idx] = False
        return max(arr) + 1

    visited = [False] * n
    visited[0] = True
    ans = re(0, visited, 0)
    print(ans)


if __name__ == "__main__":
    solve()
