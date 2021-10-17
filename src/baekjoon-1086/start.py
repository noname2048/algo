from itertools import permutations
import math

n = int(input())
num_list = [""] * n
for i in range(n):
    num_list[i] = str(input())
k = int(input())

[*candidate] = map("".join, permutations(num_list))
ans = 0
for ele in candidate:
    if int(ele) % k == 0:
        ans += 1

l = len(candidate)
gcd = math.gcd(ans, l)
print(f"{ans // gcd}/{l // gcd}")
