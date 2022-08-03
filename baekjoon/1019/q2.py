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


if __name__ == "__main__":
    pass
