from sys import stdin
import re

input = stdin.readline


def solve():
    pattern = re.compile(r"(100+1+|01)+")
    testcase = int(input())
    for i in range(testcase):
        wave = input()
        match = pattern.match(wave)
        if match and match.start() == 0 and match.end() == len(wave):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
