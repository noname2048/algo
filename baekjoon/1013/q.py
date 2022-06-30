from sys import stdin
import re


def freopen():
    def make_generator():
        s = map(
            lambda x: x.strip(),
            """4
            10010111
            011000100110001
            0110001011001
            100110001
            """.splitlines(),
        )
        yield from s

    generator = make_generator()

    def iter():
        return next(generator)

    return iter


input = stdin.readline
input = freopen()


def solve():
    pattern = re.compile(r"(100+?1+?|01)+")
    testcase = int(input())
    for _ in range(testcase):
        wave = input().strip()
        match = pattern.match(wave)
        if match and match.start() == 0 and match.end() == len(wave):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
