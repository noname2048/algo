from collections import Counter


def solve():
    n = int(input())
    counter = Counter()
    for i in range(1, n + 1):
        tmp = str(i)
        counter.update(tmp)

    total = counter.most_common(10)
    ans = [0] * 10
    for key, value in total:
        num = ord(key) - ord("0")
        ans[num] = value

    ans = " ".join([str(i) for i in ans])
    print(ans)


if __name__ == "__main__":
    solve()
