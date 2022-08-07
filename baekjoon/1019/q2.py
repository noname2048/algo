def one(n):
    ret = 0
    # quotient, remainder
    q, r = divmod(n, 10)
    k += min(n, 1) - max(n, 0)

    q, r = divmod(n, 100)
    k += q * 10
    if r >= 10:
        k += max(r - 10 + 1, 10)

    q, r = divmod(n, 1000)
    k += q * 100
    if r >= 100:
        k += max(r - 100 + 1, 100)

    count = 0
    s = 1
    topic_str, topic = s + "0", int(s + "0")
    q, r = divmod(n, topic)
    while q:
        count += q
        if r >= topic:
            count += max(r - topic + 1, 10**1)


def solve():
    n = int(input())


def test_solve():
    ns = [11, 7, 19, 199]
    ans = [
        [1, 4, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 12, 2, 2, 2, 2, 2, 2, 2, 2],
        [
            189,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
        ],
        [
            429904664,
            541008121,
            540917467,
            540117067,
            533117017,
            473117011,
            429904664,
            429904664,
            429904664,
            429904664,
        ],
    ]
    for i in range(4):
        an = solve(ns[i])
        assert (an, ans[i])


if __name__ == "__main__":

    pass
