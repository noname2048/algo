import sys

sys.stdin = open("input3.txt", "r")
# 고수의 코드
input()
(*a,) = map(int, input().split())
r = input()
f = lambda n: n - int(r) and (sum(f(i) for i, v in enumerate(a) if v == n) or 1)
print(f(a.index(-1)))
