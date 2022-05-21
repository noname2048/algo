from itertools import permutations
import math
import sys

sys.stdin = open("custom3.txt", "r")
n = int(input())
num_list = [""] * n
for i in range(n):
    num_list[i] = str(input())
k = int(input())

cand = map("".join, permutations(num_list))

ans = 0
l = 0
for ele in cand:
    l += 1
    if int(ele) % k == 0:
        ans += 1
if ans == 0:
    print("0/1")
else:
    gcd = math.gcd(ans, l)
    print(f"{ans // gcd}/{l // gcd}")
