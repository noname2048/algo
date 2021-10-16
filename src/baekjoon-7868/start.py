# x = pow(p1, i) * pow(p2, j) * pow(p3, k)
# 2 ** 60 ~= 1.8e+18
# 1 <= i + j + k <= 60

import math

p1, p2, p3, m = map(int, input().split())
num_list = [0]
for local_sum in range(1, 60 + 1):
    for i in range(local_sum + 1):
        for j in range(local_sum - i + 1):
            k = local_sum - i - j
            temp = int(math.pow(p1, i) * math.pow(p2, j) * math.pow(p3, k))
            num_list.append(temp)

num_list.sort()
print(num_list[m])
