import sys

sys.stdin = open("input1.txt", "r")

input()
[*p] = map(int, input().split())  # parent list
r = int(input())  # remove


def f(n):
    if n == r:
        return 0

    temp = sum([f(i) for i, v in enumerate(p) if v == n])

    return temp or 1  # return 1 if temp == 0 else temp


root = p.index(-1)
print(f"root({root}) = {f(root)}")
